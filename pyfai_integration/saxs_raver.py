import pyFAI
import numpy as np
import math
import SASImage
import fabio
import os
import json
import argparse
import time

def init_integration(cfg_file):
    #Load a RAW.cfg file
    raw_settings = SASImage.RawGuiSettings()
    SASImage.loadSettings(raw_settings,cfg_file)

    #Get parameters
    detector = pyFAI.detector_factory("pilatus1m")

    masks = raw_settings.get('Masks')
    mask = SASImage.createMaskMatrix(detector.shape, masks['BeamStopMask'][1])
    mask = np.logical_not(mask)

    sd_distance = raw_settings.get('SampleDistance')
    pixel_size = raw_settings.get('DetectorPixelSize')
    wavelength = raw_settings.get('WaveLength')
    bin_size = raw_settings.get('Binsize')
    normlist = raw_settings.get('NormalizationList')
    do_normalization = raw_settings.get('EnableNormalization')


    #Put everything in appropriate units
    pixel_size = pixel_size *1e-6 #convert pixel size to m
    wavelength = wavelength*1e-10 #convert wl to m


    #Set up q calibration
    xlen, ylen = detector.shape

    x_cin = raw_settings.get('Xcenter')
    y_cin = detector.shape[0]-raw_settings.get('Ycenter')

    maxlen1 = int(max(xlen - x_cin, ylen - y_cin, xlen - (xlen - x_cin), ylen - (ylen - y_cin)))

    diag1 = int(np.sqrt((xlen-x_cin)**2 + y_cin**2))
    diag2 = int(np.sqrt((x_cin**2 + y_cin**2)))
    diag3 = int(np.sqrt((x_cin**2 + (ylen-y_cin)**2)))
    diag4 = int(np.sqrt((xlen-x_cin)**2 + (ylen-y_cin)**2))

    maxlen = int(max(diag1, diag2, diag3, diag4, maxlen1)/bin_size)

    x_c = float(x_cin)
    y_c = float(y_cin)

    qmin_theta = calcTheta(sd_distance*1e-3, pixel_size, 0)
    qmin = ((4*math.pi*math.sin(qmin_theta))/(wavelength*1e10))

    qmax_theta = calcTheta(sd_distance*1e-3, pixel_size, maxlen)
    qmax = ((4*math.pi*math.sin(qmax_theta))/(wavelength*1e10))

    q_range = (qmin, qmax)

    #Set up the pyfai Aziumuthal integrator

    ai = pyFAI.AzimuthalIntegrator(detector=detector)

    ai.wavelength = wavelength
    ai.pixel1 = pixel_size
    ai.pixel2 = pixel_size
    ai.setFit2D(sd_distance, x_c, y_c)

    calibrate_dict = {'Sample_Detector_Distance'    : sd_distance,
                    'Detector_Pixel_Size'           : pixel_size,
                    'Wavelength'                    : wavelength,
                    'Beam_Center_X'                 : x_c,
                    'Beam_Center_Y'                 : y_c,
                    'Radial_Average_Method'         : 'pyFAI',
                    }

    return ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict

def pyFAIIntegrateCalibrateNormalize(img, parameters, ai, mask, q_range, maxlen,
    normlist, do_normalization, use_gpu=False):
    img_hdr = parameters['imageHeader']
    file_hdr = parameters['counters']

    # if normlist is not None and do_normalization:
    #     parameters['normalizations']['Counter_norms'] = normlist

    #     if len(normlist) == 1 and normlist[0][0] == '/':
    #         norm_val = calcExpression(normlist[0][1], img_hdr, file_hdr)
    #         pyfai_norm = True
    #     else:
    #         norm_val = 1.
    #         pyfai_norm = False

    norm_val = 1.

    #Carry out the integration
    if use_gpu:
        method = 'nosplit_csr_ocl'
    else:
        method = 'nosplit_csr'
    q, iq, errorbars = ai.integrate1d(img, maxlen, mask=mask, error_model='poisson',
        unit='q_A^-1', radial_range=q_range, method = method,
        normalization_factor=norm_val)

    i_raw = iq[:-5]        #Last points are usually garbage they're very few pixels
                        #Cutting the last 5 points here.
    q_raw = q[0:len(i_raw)]
    errorbars = errorbars[0:len(i_raw)]

    err_raw_non_nan = np.nan_to_num(errorbars)

    parameters['normalizations']['Solid_Angle_Correction'] = 'On'

    # if normlist is not None and do_normalization and not pyfai_norm:
    #     for each in normlist:
    #         op, expr = each

    #         #try:
    #         val = calcExpression(expr, img_hdr, file_hdr)

    #         if val is not None:
    #             val = float(val)
    #         else:
    #             raise ValueError
    #         if op == '/':

    #             if val == 0:
    #                raise ValueError('Divide by Zero when normalizing')

    #             i_raw = i_raw/val
    #             err_raw_non_nan = err_raw_non_nan/val

    #         elif op == '+':
    #             i_raw = i_raw + val
    #             err_raw_non_nan = err_raw_non_nan + val
    #         elif op == '*':

    #             if val == 0:
    #                raise ValueError('Multiply by Zero when normalizing')

    #             i_raw = i_raw*val
    #             err_raw_non_nan = err_raw_non_nan*val

    #         elif op == '-':
    #             i_raw = i_raw - val
    #             err_raw_non_nan = err_raw_non_nan - val

    return q_raw, i_raw, err_raw_non_nan, parameters

def doIntegration(output_dir, ai, mask, q_range, maxlen, normlist,
    do_normalization, calibrate_dict, start_point, end_point, data_file):
    print data_file
    img, img_hdr = loadImage(data_file)
    # hdrfile_info = loadHeader(data_file)
    hdrfile_info = {}

    parameters={'imageHeader'   : img_hdr,
              'counters'        : hdrfile_info,
              'filename'        : os.path.split(data_file)[1],
              'load_path'       : data_file,
              'normalizations'  : {},
              'calibration_params': calibrate_dict}


    q, i, err, parameters = pyFAIIntegrateCalibrateNormalize(img, parameters, ai,
        mask, q_range, maxlen, normlist, do_normalization)

    q = q[start_point:len(q)-end_point]
    i = i[start_point:len(i)-end_point]
    err = err[start_point:len(err)-end_point]

    output_file =os.path.join(output_dir, os.path.splitext(os.path.split(data_file)[1])[0]+'.dat')
    writeDatFile(q, i, err, parameters, output_file)

def calcExpression(expr, img_hdr, file_hdr):

        if expr != '':
            mathparser = PyMathParser()
            mathparser.addDefaultFunctions()
            mathparser.addDefaultVariables()
            mathparser.addSpecialVariables(file_hdr)
            mathparser.addSpecialVariables(img_hdr)
            mathparser.expression = expr

            val = mathparser.evaluate()
            return val
        else:
            return None

class PyMathParser(object):
    expression = ''

    functions = {'__builtins__':None};

    variables = {'__builtins__':None};

    def __init__(self):
        pass

    def evaluate(self):
        return eval(self.expression, self.variables, self.functions);

    def addSpecialVariables(self, var_dict):
        if var_dict == None:
            return

        for each_key in var_dict.keys():
            try:
                val = float(var_dict[each_key])
                self.variables[each_key] = val
            except:
                pass

    def addDefaultFunctions(self):
        self.functions['acos']=math.acos
        self.functions['asin']=math.asin
        self.functions['atan']=math.atan
        self.functions['atan2']=math.atan2
        self.functions['ceil']=math.ceil
        self.functions['cos']=math.cos
        self.functions['cosh']=math.cosh
        self.functions['degrees']=math.degrees
        self.functions['exp']=math.exp
        self.functions['fabs']=math.fabs
        self.functions['floor']=math.floor
        self.functions['fmod']=math.fmod
        self.functions['frexp']=math.frexp
        self.functions['hypot']=math.hypot
        self.functions['ldexp']=math.ldexp
        self.functions['log']=math.log
        self.functions['log10']=math.log10
        self.functions['modf']=math.modf
        self.functions['pow']=math.pow
        self.functions['radians']=math.radians
        self.functions['sin']=math.sin
        self.functions['sinh']=math.sinh
        self.functions['sqrt']=math.sqrt
        self.functions['tan']=math.tan
        self.functions['tanh']=math.tanh

    def addDefaultVariables(self):
        self.variables['pi']=math.pi

    def getVariableNames(self):
        mylist = list(self.variables.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist

    def getFunctionNames(self):
        mylist = list(self.functions.keys())
        try:
            mylist.remove('__builtins__')
        except ValueError:
            pass
        mylist.sort()
        return mylist

def calcTheta(sd_distance, pixel_size, q_length_pixels):
    if q_length_pixels == 0:
        return 0
    else:
        theta = .5 * math.atan( (q_length_pixels * pixel_size) / sd_distance )
        return theta

def loadImage(filename):
    fabio_img = fabio.open(filename)

    img = np.fliplr(fabio_img.data)
    img_hdr = fabio_img.getheader()

    if img_hdr is not None:
        img_hdr = {key.replace(' ', '_').translate(None, '()[]') if isinstance(key, str) else key: img_hdr[key] for key in img_hdr}
        img_hdr = { key : unicode(img_hdr[key], errors='ignore') if isinstance(img_hdr[key], str) else img_hdr[key] for key in img_hdr}

    return img, img_hdr

def loadHeader(filename):
    ''' returns header information based on the *image* filename
     and the type of headerfile     '''
    datadir, fname = os.path.split(filename)

    countFilename=os.path.join(datadir, '_'.join(fname.split('_')[:-1])+'.log')

    with open(countFilename,'rU') as f:
        allLines=f.readlines()

    searchName='.'.join(fname.split('.')[:-1])

    line_num=0

    test_idx = int(searchName.split('_')[-1])

    if searchName in allLines[test_idx]:
        line_num = test_idx
    else:
        for a in range(1,len(allLines)):
            if searchName in allLines[a]:
                line_num=a

    if line_num>0:
        labels=allLines[0].split('\t')
        vals=allLines[line_num].split('\t')

        hdr = {labels[a]:vals[a] for a in range(len(labels))}
    else:
        hdr = {}

    #Clean up headers by removing spaces in header names and non-unicode characters)
    if hdr is not None:
        hdr = {key.replace(' ', '_').translate(None, '()[]') if isinstance(key, str) else key : hdr[key] for key in hdr}
        hdr = {key : unicode(hdr[key], errors='ignore') if isinstance(hdr[key], str) else hdr[key] for key in hdr}

    return hdr

def writeDatFile(q, i, err, parameters, filename):
    ''' Writes an ASCII file from a measurement object, using the RAD format '''

    with open(filename, 'w') as f2:

        f2.write('### DATA:\n\n')
        f2.write('         Q               I              Error\n')
        f2.write('%d\n' % len(q))

        for idx in range(len(q)):
            line = ('%.8E %.8E %.8E\n') % (q[idx], i[idx], err[idx])
            f2.write(line)

        f2.write('\n')
        f2.write('\n')
        writeHeader(parameters, f2)

def writeHeader(d, f2, ignore_list = []):
    f2.write('### HEADER:\n\n')

    ignore_list.append('fit_sasm')
    ignore_list.append('orig_sasm')

    for ignored_key in ignore_list:
        if ignored_key in d.keys():
            del d[ignored_key]

    f2.write(json.dumps(d,indent = 4, sort_keys = True, cls = MyEncoder))

    f2.write('\n\n')

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(MyEncoder, self).default(obj)

def getNewFiles(target_dir, old_dir_list):
    dir_list = os.listdir(target_dir)

    dir_list_dict = {}

    for each_file in dir_list:
        full_path = os.path.join(target_dir, each_file)
        if os.path.splitext(each_file)[1] == '.tif':
            try:
                dir_list_dict[each_file] = (os.path.getmtime(full_path),
                    os.path.getsize(full_path))
            except OSError:
                pass

    diff_list = list(set(dir_list_dict.items()) - set(old_dir_list_dict.items()))
    diff_list.sort(key = lambda name: name[0])

    old_dir_list_dict.update(diff_list)

    return diff_list, old_dir_list_dict

########################################################################
#Run things

parser = argparse.ArgumentParser(description='Fast aziumuthal averaging of BioCAT Pilatus 1M images in a continuous fashion')
parser.add_argument('cfg', help='The SAXS configuration file (RAW format) for processing the images')
parser.add_argument('target_dir', metavar='image-dir', help='The target image directory for processing')
parser.add_argument('-o', '--output-dir', metavar='DIR', dest='output_dir', help='The output directory for integrated .dat files (default: image-dir)')

args = parser.parse_args()

if __name__ == '__main__':
    cfg_file = args.cfg

    ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict = init_integration(cfg_file)

    start_point = raw_settings.get('StartPoint')
    end_point = raw_settings.get('EndPoint')

    target_dir = args.target_dir
    old_dir_list_dict = {}

    if args.output_dir is not None:
        output_dir = args.output_dir
    else:
        output_dir = target_dir

    while True:
        try:

            diff_list, old_dir_list_dict = getNewFiles(target_dir, old_dir_list_dict)

            if not diff_list:
                time.sleep(0.01)
            else:
                [doIntegration(output_dir, ai, mask, q_range, maxlen, normlist,
                    do_normalization, calibrate_dict, start_point, end_point,
                    os.path.join(target_dir, name)) for name, stuff in diff_list]

        except KeyboardInterrupt:
            break