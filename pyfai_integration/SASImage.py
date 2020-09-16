'''
Created on Jul 7, 2010

@author: specuser
'''
import json
import cPickle
import copy

import numpy as np
from scipy import optimize

import polygonMasking as polymask

#modified
class RawGuiSettings(object):
    '''
    This object contains all the settings nessecary for the GUI.

    '''
    def __init__(self, settings = None):
        '''
        Accepts a dictionary argument for the parameters. Uses default is no settings are given.
        '''

        self._params = settings

        if settings == None:
            self._params = {
                            'NormFlatfieldEnabled'  : [False,    'bool'],

                            'NormAbsWater'          : [False,    'bool'],
                            'NormAbsWaterI0'        : [0.01632,  'float'],
                            'NormAbsWaterTemp'      : ['25',     'choice'],
                            'NormAbsWaterConst'     : [1.0,      'float'],
                            'NormAbsWaterFile'      : [None, 'text'],
                            'NormAbsWaterEmptyFile' : [None, 'text'],
                            'NormFlatfieldFile'     : [None, 'text'],

                            'NormAbsCarbon'             : [False, 'bool'],
                            'NormAbsCarbonIgnoreBkg'    : [True, 'bool'],
                            'NormAbsCarbonFile'         : [None, 'text'],
                            'NormAbsCarbonEmptyFile'    : [None, 'text'],
                            'NormAbsCarbonSamEmptyFile' : [None, 'text'],
                            'NormAbsCarbonCalFile'      : [None, 'text'],
                            'NormAbsCarbonThick'        : [1.055, 'float'],
                            'NormAbsCarbonSamThick'     : [1.0, 'float'],
                            'NormAbsCarbonUpstreamCtr'  : [None, 'choice'],
                            'NormAbsCarbonDownstreamCtr': [None, 'choice'],
                            'NormAbsCarbonConst'        : [1.0, 'float'],
                            'NormAbsCarbonSamEmptySASM' : [None],


                            'NormalizeTrans'    : [False,  'bool'],
                            'Calibrate'         : [False,  'bool'],  # Calibrate AgBe
                            'CalibrateMan'      : [True,  'bool'],  # Calibrate manual (wavelength / distance)
                            'AutoBgSubtract'    : [False,  'bool'],
                            'CountNormalize'    : [1.0,   'float'],

                            'AutoBIFT'          : [False, 'bool'],
                            'AutoAvg'           : [False, 'bool'],
                            'AutoAvgRemovePlots': [False, 'bool'],

                            'AutoAvgRegExp'     : ['', 'text'],
                            'AutoAvgNameRegExp' : ['', 'text'],
                            'AutoAvgNoOfFrames' : [1,   'int'],
                            'AutoBgSubRegExp'   : ['', 'text'],

                            'UseHeaderForMask': [False, 'bool'],
                            'DetectorFlipped90':[False, 'bool'],
                            'DetectorFlipLR' : [True, 'bool'],
                            'DetectorFlipUD' : [False, 'bool'],

                            #CORRECTIONS
                            'DoSolidAngleCorrection' : [True, 'bool'],


                            #CENTER / BINNING
                            'Binsize'    : [1,     'int'],
                            'Xcenter'    : [512.0, 'float'],
                            'Ycenter'    : [512.0, 'float'],
                            'QrangeLow'  : [25,    'int'],
                            'QrangeHigh' : [9999,  'int'],
                            'StartPoint' : [0,     'int'],
                            'EndPoint'   : [0,     'int'],
                            'ImageDim'   : [[1024,1024]],

                            #MASKING
                            'SampleFile'              : [None, 'text'],
                            'BackgroundSASM'          : [None, 'text'],

                            'DataSECM'                : [None, 'text'],

                            'TransparentBSMask'       : [None],
                            'TransparentBSMaskParams' : [None],
                            'BeamStopMask'            : [None],
                            'BeamStopMaskParams'      : [None],
                            'ReadOutNoiseMask'        : [None],
                            'ReadOutNoiseMaskParams'  : [None],
                                                                                #mask, mask_patches
                            'Masks'                   : [{'BeamStopMask'     : [None, None],
                                                          'ReadOutNoiseMask' : [None, None],
                                                          'TransparentBSMask': [None, None],
                                                         }],

                            'MaskDimension'          : [1024,1024],

                            #Q-CALIBRATION
                            'WaveLength'          : [1.0,  'float'],
                            'SampleDistance'      : [1000, 'float'],
                            'ReferenceQ'          : [0.0, 'float'],
                            'ReferenceDistPixel'  : [0,   'int'],
                            'ReferenceDistMm'     : [0.0, 'float'],
                            'DetectorPixelSize'   : [70.5, 'float'],
                            'SmpDetectOffsetDist' : [0.0, 'float'],


                            #SANS Parameters
                            'SampleThickness'       : [0.1,  'float'],
                            'DarkCorrEnabled'       : [False,    'bool'],
                            'DarkCorrFilename'      : [None, 'text'],


                            #DEFAULT BIFT PARAMETERS
                            'maxDmax'     : [400.0,  'float'],
                            'minDmax'     : [10.0,   'float'],
                            'DmaxPoints'  : [10,     'int'],
                            'maxAlpha'    : [1e10,   'float'],
                            'minAlpha'    : [150.0,  'float'],
                            'AlphaPoints' : [16,     'int'],
                            'PrPoints'    : [50,     'int'],

                            #DEFAULT pyGNOM PARAMETERS
                            'pygnomMaxAlpha'    : [60,   'float'],
                            'pygnomMinAlpha'    : [0.01, 'float'],
                            'pygnomAlphaPoints' : [100,  'int'],
                            'pygnomPrPoints'    : [50,   'int'],
                            'pygnomFixInitZero' : [True, 'bool'],

                            'pyOSCILLweight'    : [3.0, 'float'],
                            'pyVALCENweight'    : [1.0, 'float'],
                            'pyPOSITVweight'    : [1.0, 'float'],
                            'pySYSDEVweight'    : [3.0, 'float'],
                            'pySTABILweight'    : [3.0, 'float'],
                            'pyDISCRPweight'    : [1.0, 'float'],

                            #DEFAULT IFT PARAMETERS:
                            'IFTAlgoList'        : [['BIFT', 'pyGNOM']],
                            'IFTAlgoChoice'      : [['BIFT']],

                            #ARTIFACT REMOVAL:
                            'ZingerRemovalRadAvg'    : [False, 'bool'],
                            'ZingerRemovalRadAvgStd' : [4.0,     'float'],

                            'ZingerRemoval'     : [False, 'bool'],
                            'ZingerRemoveSTD'   : [4,     'int'],
                            'ZingerRemoveWinLen': [10,    'int'],
                            'ZingerRemoveIdx'   : [10,    'int'],

                            'ZingerRemovalAvgStd'  : [8,     'int'],
                            'ZingerRemovalAvg'     : [False, 'bool'],

                            #SAVE DIRECTORIES
                            'ProcessedFilePath'    : [None,  'text'],
                            'AveragedFilePath'     : [None,  'text'],
                            'SubtractedFilePath'   : [None,  'text'],
                            'BiftFilePath'         : [None,  'text'],
                            'GnomFilePath'         : [None,  'text'],
                            'AutoSaveOnImageFiles' : [False, 'bool'],
                            'AutoSaveOnAvgFiles'   : [False, 'bool'],
                            'AutoSaveOnSub'        : [False, 'bool'],
                            'AutoSaveOnBift'       : [False, 'bool'],
                            'AutoSaveOnGnom'       : [False, 'bool'],


                            'ImageHdrList'         : [None],
                            'FileHdrList'          : [None],

                            'UseHeaderForCalib'    : [False, 'bool'],

                            # Header bind list with [(Description : parameter key, header_key)]
                            'HeaderBindList'       : [{'Beam X Center'            : ['Xcenter',           None, ''],
                                                       'Beam Y Center'            : ['Ycenter',           None, ''],
                                                       'Sample Detector Distance' : ['SampleDistance',    None, ''],
                                                       'Wavelength'               : ['WaveLength',        None, ''],
                                                       'Detector Pixel Size'      : ['DetectorPixelSize', None, '']}],
                                                       # 'Number of Frames'         : ['NumberOfFrames',    None, '']}],

                            'NormalizationList'    : [None, 'text'],
                            'EnableNormalization'  : [True, 'bool'],

                            'OnlineFilterList'     : [None, 'text'],
                            'EnableOnlineFiltering': [False, 'bool'],
                            'OnlineModeOnStartup'  : [False, 'bool'],
                            'OnlineStartupDir'     : [None, 'text'],

                            'MWStandardMW'         : [0, 'float'],
                            'MWStandardI0'         : [0, 'float'],
                            'MWStandardConc'       : [0, 'float'],
                            'MWStandardFile'       : ['', 'text'],

                            #Initialize volume of correlation molecular mass values.
                            #Values from Rambo, R. P. & Tainer, J. A. (2013). Nature. 496, 477-481.
                            'MWVcType'             : ['Protein', 'choice'],
                            'MWVcAProtein'         : [1.0, 'float'], #The 'A' coefficient for proteins
                            'MWVcBProtein'         : [0.1231, 'float'], #The 'B' coefficient for proteins
                            'MWVcARna'             : [0.808, 'float'], #The 'A' coefficient for proteins
                            'MWVcBRna'             : [0.00934, 'float'], #The 'B' coefficient for proteins

                            #Initialize porod volume molecularm ass values.
                            'MWVpRho'              : [0.83*10**(-3), 'float'], #The density in kDa/A^3

                            #Initialize Absolute scattering calibration values.
                            #Default values from Mylonas & Svergun, J. App. Crys. 2007.
                            'MWAbsRhoMprot'         : [3.22*10**23, 'float'], #e-/g, # electrons per dry mass of protein
                            'MWAbsRhoSolv'          : [3.34*10**23, 'float'], #e-/cm^-3, # electrons per volume of aqueous solvent
                            'MWAbsNuBar'            : [0.7425, 'float'], #cm^3/g, # partial specific volume of the protein
                            'MWAbsR0'               : [2.8179*10**-13, 'float'], #cm, scattering lenght of an electron

                            'CurrentCfg'         : [None],
                            'CompatibleFormats'  : [['.rad', '.tiff', '.tif', '.img', '.csv', '.dat', '.txt', '.sfrm', '.dm3', '.edf',
                                                     '.xml', '.cbf', '.kccd', '.msk', '.spr', '.h5', '.mccd', '.mar3450', '.npy', '.pnm',
                                                      '.No', '.imx_0', '.dkx_0', '.dkx_1', '.png', '.mpa', '.ift', '.sub', '.fit', '.fir',
                                                      '.out', '.mar1200', '.mar2400', '.mar2300', '.mar3600', '.int', '.ccdraw'], None],


                            #SEC Settings:
                            'secCalcThreshold'      : [1.02, 'float'],

                            #GUI Settings:
                            'csvIncludeData'      : [None],
                            'ManipItemCollapsed'  : [False, 'bool'] ,
                            'CurrentFilePath'     : [None],


                            'DatHeaderOnTop'      : [False, 'bool'],
                            'PromptConfigLoad'    : [True, 'bool'],

                            #ATSAS settings:
                            'autoFindATSAS'       : [True, 'bool'],
                            'ATSASDir'            : ['', 'bool'],

                            #GNOM settings
                            'gnomExpertFile'        : ['', 'text'],
                            'gnomForceRminZero'     : ['Y', 'choice'],
                            'gnomForceRmaxZero'     : ['Y', 'choice'],
                            'gnomNPoints'           : [171, 'int'],
                            'gnomInitialAlpha'      : [0.0, 'float'],
                            'gnomAngularScale'      : [1, 'int'],
                            'gnomSystem'            : [0, 'int'],
                            'gnomFormFactor'        : ['', 'text'],
                            'gnomRadius56'          : [-1, 'float'],
                            'gnomRmin'              : [-1, 'float'],
                            'gnomFWHM'              : [-1, 'float'],
                            'gnomAH'                : [-1, 'float'],
                            'gnomLH'                : [-1, 'float'],
                            'gnomAW'                : [-1, 'float'],
                            'gnomLW'                : [-1, 'float'],
                            'gnomSpot'              : ['', 'text'],
                            'gnomExpt'              : [0, 'int'],

                            #DAMMIF settings
                            'dammifMode'            : ['Slow', 'choice'],
                            'dammifSymmetry'        : ['P1', 'choice'],
                            'dammifAnisometry'      : ['Unknown', 'choice'],
                            'dammifUnit'            : ['Unknown', 'choice'],
                            'dammifChained'         : [False, 'bool'],
                            'dammifConstant'        : ['', 'text'],
                            'dammifOmitSolvent'     : [True, 'bool'],
                            'dammifDummyRadius'     : [-1, 'float'],
                            'dammifSH'              : [-1, 'int'],
                            'dammifPropToFit'       : [-1, 'float'],
                            'dammifKnots'           : [-1, 'int'],
                            'dammifCurveWeight'     : ['e', 'choice'],
                            'dammifRandomSeed'      : ['', 'text'],
                            'dammifMaxSteps'        : [-1, 'int'],
                            'dammifMaxIters'        : [-1, 'int'],
                            'dammifMaxStepSuccess'  : [-1, 'int'],
                            'dammifMinStepSuccess'  : [-1, 'int'],
                            'dammifTFactor'         : [-1, 'float'],
                            'dammifRgPen'           : [-1, 'float'],
                            'dammifCenPen'          : [-1, 'float'],
                            'dammifLoosePen'        : [-1, 'float'],
                            'dammifAnisPen'         : [-1, 'float'],
                            'dammifMaxBeadCount'    : [-1, 'int'],
                            'dammifReconstruct'     : [15, 'int'],
                            'dammifDamaver'         : [True, 'bool'],
                            'dammifDamclust'        : [False, 'bool'],
                            'dammifRefine'          : [True, 'bool'],
                            'dammifProgram'         : ['DAMMIF', 'choice'],
                            'dammifExpectedShape'   : ['u', 'choice'],

                            #DAMMIN settings that are not included in DAMMIF settings
                            'damminInitial'         : ['S', 'choice'], #Initial DAM
                            'damminKnots'           : [20, 'int'],
                            'damminConstant'        : [0, 'float'],
                            'damminDiameter'        : [-1, 'float'],
                            'damminPacking'         : [-1, 'float'],
                            'damminCoordination'    : [-1, 'float'],
                            'damminDisconPen'       : [-1, 'float'],
                            'damminPeriphPen'       : [-1, 'float'],
                            'damminCurveWeight'     : ['1', 'choice'],
                            'damminAnealSched'      : [-1, 'float'],

                            #Weighted Average Settings
                            'weightCounter'         : ['', 'choice'],
                            'weightByError'         : [True, 'bool'],

                            #Similarity testing settings
                            'similarityTest'        : ['CorMap', 'choice'],
                            'similarityCorrection'  : ['Bonferroni', 'choice'],
                            'similarityThreshold'   : [0.01, 'float'],
                            'similarityOnAverage'   : [True, 'bool'],

                            #Fitting settings
                            'errorWeight'           : [True, 'bool'],

                            #Denss settings
                            'denssVoxel'            : [5, 'float'],
                            'denssOversampling'     : [3, 'float'],
                            'denssNElectrons'       : ['', 'text'],
                            'denssSteps'            : [10000, 'int'],
                            'denssLimitDmax'        : [False, 'bool'],
                            'denssDmaxStartStep'    : [500, 'int'],
                            'denssRecenter'         : [True, 'bool'],
                            'denssRecenterStep'     : ['[1001,1501,3001,5001,6001,7001,8001]', 'text'],
                            'denssPositivity'       : [True, 'bool'],
                            'denssExtrapolate'      : [True, 'bool'],
                            'denssShrinkwrap'       : [True, 'bool'],
                            'denssShrinkwrapSigmaStart' : [3, 'float'],
                            'denssShrinkwrapSigmaEnd'   : [1.5, 'float'],
                            'denssShrinkwrapSigmaDecay' : [0.99, 'float'],
                            'denssShrinkwrapThresFrac'  : [0.20, 'float'],
                            'denssShrinkwrapIter'   : [20, 'int'],
                            'denssShrinkwrapMinStep'    : [5000, 'int'],
                            'denssConnected'        : [True, 'bool'],
                            'denssConnectivitySteps'    : ['[7500]', 'text'],
                            'denssChiEndFrac'       : [0.001, 'float'],
                            'denssPlotOutput'       : [True, 'bool'],
                            'denssEman2Average'     : [True, 'bool'],
                            'denssReconstruct'      : [20, 'int'],
                            'EMAN2Dir'              : ['', 'text'],
                            'autoFindEMAN2'         : [True, 'bool'],
                            'denssCutOut'           : [False, 'bool'],
                            'denssWriteXplor'       : [True, 'bool'],
                            'denssMode'             : ['Slow', 'choice'],
                            'denssRecenterMode'     : ['com', 'choice'],
                            'denssEnantiomer'       : [True, 'bool'],

                            }

    def get(self, key):
        return self._params[key][0]

    def set(self, key, value):
        self._params[key][0] = value

    def getId(self, key):
        return self._params[key][1]

    def getType(self, key):
        return self._params[key][2]

    def getIdAndType(self, key):
        return (self._params[key][1], self._params[key][2])

    def getAllParams(self):
        return self._params

class Mask():
    ''' Mask super class. Masking is used for masking out unwanted regions
    of an image '''

    def __init__(self, mask_id, img_dim, mask_type, negative = False):

        self._is_negative_mask = negative
        self._img_dimension = img_dim            # need image Dimentions to get the correct fill points
        self._mask_id = mask_id
        self._type = mask_type
        self._points = None

    def setAsNegativeMask(self):
        self._is_negative_mask = True

    def setAsPositiveMask(self):
        self._is_negative_mask = False

    def isNegativeMask(self):
        return self._is_negative_mask

    def getPoints(self):
        return self._points

    def setPoints(self, points):
        self._points = points

    def setId(self, id):
        self._mask_id = id

    def getId(self):
        return self._mask_id

    def getType(self):
        return self._type

    def getFillPoints(self):
        pass    # overridden when inherited

    def getSaveFormat(self):
        pass   # overridden when inherited

class CircleMask(Mask):
    ''' Create a circular mask '''

    def __init__(self, center_point, radius_point, id, img_dim, negative = False):

        Mask.__init__(self, id, img_dim, 'circle', negative)

        self._points = [center_point, radius_point]
        self._radius = abs(self._points[1][0] - self._points[0][0])

    def getRadius(self):
        return self._radius

    def grow(self, pixels):
        ''' Grow the circle by extending the radius by a number
        of pixels '''

        xy_c, xy_r = self._points

        x_c, y_c = xy_c
        x_r, y_r = xy_r

        if x_r > x_c:
            x_r = x_r + pixels
        else:
            x_r = x_r - pixels

        self.setPoints([(x_c,y_c), (x_r,y_r)])

    def shrink(self, pixels):
        ''' Shrink the circle by shortening the radius by a number
        of pixels '''

        xy_c, xy_r = self._points

        x_c, y_c = xy_c
        x_r, y_r = xy_r

        if x_r > x_c:
            x_r = x_r - pixels
        else:
            x_r = x_r + pixels

        self.setPoints([(x_c,y_c), (x_r,y_r)])

    def setPoints(self, points):
        self._points = points
        self.radius = abs(points[1][0] - points[0][0])

    def getFillPoints(self):
        ''' Really Clumsy! Can be optimized alot! triplicates the points in the middle!'''

        radiusC = abs(self._points[1][0] - self._points[0][0])

        P = calcBresenhamCirclePoints(radiusC, self._points[0][1], self._points[0][0])

        fillPoints = []

        for i in range(0, int(len(P)/8) ):
            Pp = P[i*8 : i*8 + 8]

            q_ud1 = ( Pp[0][0], range( int(Pp[1][1]), int(Pp[0][1]+1)) )
            q_ud2 = ( Pp[2][0], range( int(Pp[3][1]), int(Pp[2][1]+1)) )

            q_lr1 = ( Pp[4][1], range( int(Pp[6][0]), int(Pp[4][0]+1)) )
            q_lr2 = ( Pp[5][1], range( int(Pp[7][0]), int(Pp[5][0]+1)) )

            for i in range(0, len(q_ud1[1])):
                fillPoints.append( (int(q_ud1[0]), int(q_ud1[1][i])) )
                fillPoints.append( (int(q_ud2[0]), int(q_ud2[1][i])) )
                fillPoints.append( (int(q_lr1[1][i]), int(q_lr1[0])) )
                fillPoints.append( (int(q_lr2[1][i]), int(q_lr2[0])) )

        return fillPoints

    def getSaveFormat(self):
        save = {'type'          :   self._type,
                'center_point'  :   self._points[0],
                'radius_point'  :   self._points[1],
                'negative'      :   self._is_negative_mask,
                }
        return save

class RectangleMask(Mask):
    ''' create a retangular mask '''

    def __init__(self, first_point, second_point, id, img_dim, negative = False):

        Mask.__init__(self, id, img_dim, 'rectangle', negative)
        self._points = [first_point, second_point]

    def grow(self, pixels):

        xy1, xy2 = self._points

        x1, y1 = xy1
        x2, y2 = xy2

        if x1 > x2:
            x1 = x1 + pixels
            x2 = x2 - pixels
        else:
            x1 = x1 - pixels
            x2 = x2 + pixels

        if y1 > y2:
            y1 = y1 - pixels
            y2 = y2 + pixels
        else:
            y1 = y1 + pixels
            y2 = y2 - pixels

        self._points = [(x1,y1), (x2,y2)]

    def shrink(self):
        ''' NOT IMPLEMENTED YET '''
        pass

    def getFillPoints(self):

        self.startPoint, self.endPoint = self._points
        '''  startPoint and endPoint: [(x1,y1) , (x2,y2)]  '''

        startPointX = int(self.startPoint[1])
        startPointY = int(self.startPoint[0])

        endPointX = int(self.endPoint[1])
        endPointY = int(self.endPoint[0])

        fillPoints = []

        if startPointX > endPointX:

            if startPointY > endPointY:

                for c in range(endPointY, startPointY + 1):
                    for i in range(endPointX, startPointX + 1):
                        fillPoints.append( (int(i), int(c)) )
            else:
                for c in range(startPointY, endPointY + 1):
                    for i in range(endPointX, startPointX + 1):
                        fillPoints.append( (int(i), int(c)) )

        else:

            if startPointY > endPointY:

                for c in range(endPointY, startPointY + 1):
                    for i in range(startPointX, endPointX + 1):
                        fillPoints.append( (int(i),int(c)) )
            else:
                for c in range(startPointY, endPointY + 1):
                    for i in range(startPointX, endPointX + 1):
                        fillPoints.append( (int(i), int(c)) )

        return fillPoints

    def getSaveFormat(self):
        save = {'type'          :   self._type,
                'first_point'   :   self._points[0],
                'second_point'  :   self._points[1],
                'negative'      :   self._is_negative_mask,
                }
        return save

class PolygonMask(Mask):
    ''' create a polygon mask '''

    def __init__(self, points, id, img_dim, negative = False):

        Mask.__init__(self, id, img_dim, 'polygon', negative)

        self._points = points

    def getFillPoints(self):

        proper_formatted_points = []
        yDim, xDim = self._img_dimension

        for each in self._points:
            proper_formatted_points.append(list(each))

        proper_formatted_points = np.array(proper_formatted_points)

        pb = polymask.Polygeom(proper_formatted_points)

        grid = np.mgrid[0:xDim,0:yDim].reshape(2,-1).swapaxes(0,1)

        inside = pb.inside(grid)

        p = np.where(inside==True)

        coords = polymask.getCoords(p, (int(yDim), int(xDim)))

        return coords

    def getSaveFormat(self):
        save = {'type'      :   self._type,
                'vertices'  :   self._points,
                'negative'  :   self._is_negative_mask,
                }
        return save

def calcBresenhamCirclePoints(radius, xOffset = 0, yOffset = 0):
    ''' Uses the Bresenham circle algorithm for determining the points
     of a circle with a certain radius '''

    x = 0
    y = radius

    switch = 3 - (2 * radius)
    points = []
    while x <= y:
        points.extend([(x + xOffset, y + yOffset),(x + xOffset,-y + yOffset),
                       (-x + xOffset, y + yOffset),(-x + xOffset,-y + yOffset),
                       (y + xOffset, x + yOffset),(y + xOffset,-x + yOffset),
                       (-y + xOffset, x + yOffset),(-y + xOffset, -x + yOffset)])
        if switch < 0:
            switch = switch + (4 * x) + 6
        else:
            switch = switch + (4 * (x - y)) + 10
            y = y - 1
        x = x + 1

    return points

#modified
def createMaskMatrix(img_dim, masks):
    ''' creates a 2D binary matrix of the same size as the image,
    corresponding to the mask pattern '''

    negmasks = []
    posmasks = []
    neg = False

    for each in masks:
        if each.isNegativeMask() == True:
            neg = True
            negmasks.append(each)
        else:
            posmasks.append(each)

    if neg:
        for each in posmasks:
            negmasks.append(each)

            masks = negmasks
        mask = np.zeros(img_dim)
    else:
        mask = np.ones(img_dim)

    maxy = mask.shape[1]
    maxx = mask.shape[0]

    for each in masks:
        fillPoints = each.getFillPoints()

        if each.isNegativeMask() == True:
            for eachp in fillPoints:
                if eachp[0] < maxx and eachp[0] >= 0 and eachp[1] < maxy and eachp[1] >= 0:
                    y = int(eachp[1])
                    x = int(eachp[0])
                    mask[(x,y)] = 1
        else:
            for eachp in fillPoints:
                if eachp[0] < maxx and eachp[0] >= 0 and eachp[1] < maxy and eachp[1] >= 0:
                    y = int(eachp[1])
                    x = int(eachp[0])
                    mask[(x,y)] = 0

    #Mask is flipped (older RAW versions had flipped image)
    mask = np.flipud(mask)

    return mask

# def loadSettings(raw_settings, loadpath):

#     file_obj = open(loadpath, 'rb')
#     loaded_param = cPickle.load(file_obj)
#     file_obj.close()

#     keys = loaded_param.keys()
#     all_params = raw_settings.getAllParams()

#     for each_key in keys:
#         if each_key in all_params:
#             all_params[each_key][0] = copy.copy(loaded_param[each_key])

#     # main_frame = wx.FindWindowByName('MainFrame')
#     # main_frame.queueTaskInWorkerThread('recreate_all_masks', None)

#     # fixBackwardsCompatibility(raw_settings)

    # return True

def readSettings(filename):

    try:
        with open(filename, 'r') as f:
            settings = f.read()
        settings = dict(json.loads(settings))
    except Exception as e:
        print e
        try:
            with open(filename, 'rb') as f:
                settings = cPickle.load(f)
        except (KeyError, EOFError, ImportError, IndexError, AttributeError, cPickle.UnpicklingError) as e:
            print 'Error type: %s, error: %s' %(type(e).__name__, e)
            return None

    return settings

def loadSettings(raw_settings, loadpath):

    loaded_param = readSettings(loadpath)

    if loaded_param is None:
        return False

    keys = loaded_param.keys()
    all_params = raw_settings.getAllParams()

    for each_key in keys:
        if each_key in all_params:
            all_params[each_key][0] = copy.copy(loaded_param[each_key])

    default_settings = RawGuiSettings().getAllParams()

    for key in default_settings.keys():
        if key not in loaded_param:
            all_params[key] = default_settings[key]

    postProcess(raw_settings)

    return True

def postProcess(raw_settings):

    masks = copy.copy(raw_settings.get('Masks'))

    for mask_type in masks.keys():
        mask_list = masks[mask_type][1]
        if mask_list is not None:
            img_dim = raw_settings.get('MaskDimension')

            for i, mask in enumerate(mask_list):
                if isinstance(mask, dict):
                    if mask['type'] == 'circle':
                        mask = CircleMask(mask['center_point'],
                            mask['radius_point'], i, img_dim, mask['negative'])
                    elif mask['type'] == 'rectangle':
                        mask = RectangleMask(mask['first_point'],
                            mask['second_point'], i, img_dim, mask['negative'])
                    elif mask['type'] == 'polygon':
                        mask = PolygonMask(mask['vertices'], i, img_dim,
                            mask['negative'])
                mask_list[i] = mask

            masks[mask_type][1] = mask_list

    raw_settings.set('Masks', masks)

    return
