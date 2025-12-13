import os
import glob
import sys
import time

import bioxtasraw.RAWAPI as raw

def getNewFiles(target_dir, output_dir, fprefix, extra_target_name, target_ext,
    extra_output_name, output_ext, overwrite):
    # print 'Getting New Files'
    target_dir_list = os.listdir(target_dir)

    target_f_list = []

    for each_file in target_dir_list:
        if os.path.splitext(each_file)[1].lstrip('.') == target_ext and extra_target_name in os.path.split(each_file)[1]:
            if fprefix is None or each_file.startswith(fprefix):
                target_f_list.append(each_file)

    if not overwrite:
        output_dir_list = os.listdir(output_dir)

        output_f_list = []

        for each_file in output_dir_list:
            if os.path.splitext(each_file)[1].lstrip('.') == output_ext and extra_output_name in os.path.split(each_file)[1]:
                if fprefix is None or each_file.startswith(fprefix):
                    fname = os.path.splitext(each_file)[0]
                    img_name = '_'.join(fname.split('_')[:-1])+'.'+target_ext
                    output_f_list.append(img_name)

        diff_list = list(set(target_f_list) - set(output_f_list))
        diff_list.sort()

    else:
        diff_list = target_f_list
        diff_list.sort()

    return diff_list


#New batch definition:
#[
#images dir,
#images prefix,
#profiles output dir,
#mask dir,
#mask prefix
#]

# December 2025, Grubic

batch_list = [
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG03',
    'TG03',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG03/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_12/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG04',
    'TG04',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG04/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_12/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG05',
    'TG05',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG05/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_12/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG06',
    'TG06',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG06/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_13/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG07',
    'TG07',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG07/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_13/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG08',
    'TG08',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG08/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_13/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG09',
    'TG09',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG09/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_13/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG01',
    'TG01',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG01/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_12/',
    'TG'
    ],
    ['/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/TG02',
    'TG02',
    '/nas_data/SAXS/2025_Run3/2025_12_12_Grubic/TG02/profiles',
    '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/masks_12_12/',
    'TG'
    ],
    ]

# Overwrite files or just do the new ones?
overwrite = False

#Eiger
img_ext = 'h5'
zpad = 6
extra_name = 'data'


for source_dir, fprefix, output_dir, mask_dir, mask_prefix in batch_list:
    print(fprefix)

    try:

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print('Getting file list')
        diff_list = getNewFiles(source_dir, output_dir, fprefix, extra_name,
            img_ext, '', 'dat', overwrite)

        # Chaotic flow
        f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_{}*.{}'.format(fprefix, extra_name, img_ext)))
        fnum_list = list(set([int(fname.split('_')[-1].rstrip('{}'.format(img_ext)).rstrip('.')) for fname in f_list]))
        fnum_list.sort()

        print('Processing images')

        gen_config_results = raw.load_settings(os.path.join(mask_dir, '{}_basic.cfg'.format(mask_prefix)))

        for fnum in fnum_list:
            print(fnum)
            print('Loading config file')
            if os.path.exists(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum))):
                raw_settings = raw.load_settings(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum)))
                # print('point config')
            else:
                raw_settings = gen_config_results
                # print('generic config')

            done_list = []

            for name in diff_list:

                file_fnum = int(os.path.splitext(name)[0].split('_')[-1])

                if file_fnum == fnum:
                    print(name)

                    dats, _ = raw.load_and_integrate_images([os.path.join(source_dir,name)], raw_settings)
                    data = dats[0]

                    raw.save_profile(data, settings=raw_settings, datadir=output_dir)

                    done_list.append(name)

            for name in done_list:
                diff_list.remove(name)

            if raw_settings != gen_config_results:
                del raw_settings

        del gen_config_results

    except KeyboardInterrupt:
        break

    # try:
    #     old_dir_list_dict = {}

    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)

    #     print('Getting file list')
    #     diff_list, old_dir_list_dict = getNewFiles(source_dir, old_dir_list_dict, fprefix, extra_name, img_ext)
    #     print('Loading config files')
    #     # Chaotic flow
    #     f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_{}*.{}'.format(fprefix, extra_name, img_ext)))
    #     fnum_list = list(set([int(fname.split('_')[-1].rstrip('{}'.format(img_ext)).rstrip('.')) for fname in f_list]))
    #     fnum_list.sort()

    #     # print(fnum_list)

    #     # # Laminar flow
    #     # # f_list = glob.glob(os.path.join(source_dir, '{}_???_s???_0001_*.tif'.format(fprefix)))
    #     # f_list = glob.glob(os.path.join(source_dir, '{}_???_s???_0001_*.tif'.format(fprefix)))
    #     # if len(f_list) == 0:
    #     #     f_list = glob.glob(os.path.join(source_dir, '{}_???_s????_0001_*.tif'.format(fprefix)))
    #     # fnum_list = list(set([int(fname.split('_')[-1].strip('.tif')) for fname in f_list]))
    #     # fnum_list.sort()
    #     # step_list = list(set([fname.split('_')[-3] for fname in f_list]))
    #     # step_list.sort()

    #     config_dict = {}

    #     # Chaotic flow August 2019 and December 2019
    #     # if 'martin' in source_dir:
    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'pinto' in source_dir:
    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'sosnick' in source_dir:
    #     #     if len(fnum_list) == 30:
    #     #         prefix='short'
    #     #     else:
    #     #         prefix='long'

    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_basic.cfg'.format(prefix)))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'cytc' in source_dir:
    #     #     # if fprefix in ['native_cytc1', 'native_buffer1']:
    #     #     #     prefix = 'native'
    #     #     # elif fprefix in ['buffer2', 'buffer3', 'cytc2', 'cytc3']:
    #     #     #     prefix = '0808'
    #     #     # elif fprefix in ['buffer4' , 'buffer5', 'cytc4', 'cytc5']:
    #     #     #     prefix = '0809'

    #     #     # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_basic.cfg'.format(prefix)))

    #     #     # for fnum in fnum_list:
    #     #     #     if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum))):
    #     #     #         config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum)))
    #     #     #     else:
    #     #     #         config_results = gen_config_results

    #     #     #     config_dict[fnum] = config_results

    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results


    #     # # December 2019
    #     # if 'martin' in source_dir.lower():
    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))):
    #     #                 # print os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results

    #     # elif 'pinto' in source_dir.lower():
    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'jp_basic_{:04d}.cfg'.format(fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum))):
    #     #                 # print os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results

    #     # elif '/na/' in source_dir.lower():
    #     #     na_list = ['ric_mgs_01', 'ric_01', 'ric452_mgs_01']
    #     #     na2_list = ['buf_01', 'ric452_mgs_02', 'ric452_mgs_03', 'ric452_01',
    #     #                     'ric_mgo_01', 'ric_mgo_02', 'buf_02', 'ric452_mgo_01', 'buf_03']

    #     #     if fprefix in na_list:
    #     #         cfg_prefix = 'na'
    #     #     elif fprefix in na2_list:
    #     #         cfg_prefix = 'na2'

    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, '{}_basic_{:04d}.cfg'.format(cfg_prefix, fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(cfg_prefix, step, fnum))):
    #     #                 # print os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(cfg_prefix, step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results


    #     # # Laminar flow Dec. 2021
    #     # run_num = int(source_dir.split('/')[-1].lstrip('RM'))

    #     # if 1 <= run_num and run_num <= 5:
    #     #     sub_mask_dir = 'rm01_05'
    #     # elif run_num == 6:
    #     #     sub_mask_dir = 'rm06'
    #     # elif 8 <= run_num and run_num <= 10:
    #     #     sub_mask_dir = 'rm08_10'
    #     # elif 12 <= run_num and run_num <= 13:
    #     #     sub_mask_dir = 'rm12_13'
    #     # elif run_num == 15:
    #     #     sub_mask_dir = 'rm15'
    #     # elif run_num == 16:
    #     #     sub_mask_dir = 'rm16'
    #     # elif 17 <= run_num and run_num <= 20:
    #     #     sub_mask_dir = 'rm17_20'
    #     # elif run_num == 21:
    #     #     sub_mask_dir = 'rm21'
    #     # elif run_num == 22:
    #     #     sub_mask_dir = 'rm22'

    #     # gen_config_results = raw.load_settings(os.path.join(base_config_dir, sub_mask_dir, 'rm_basic.cfg'))

    #     # for fnum in fnum_list:
    #     #     if os.path.exists(os.path.join(base_config_dir, sub_mask_dir, 'rm_{:04d}.cfg'.format(fnum))):
    #     #         config_results = raw.load_settings(os.path.join(base_config_dir, sub_mask_dir, 'rm_{:04d}.cfg'.format(fnum)))
    #     #     else:
    #     #         config_results = gen_config_results

    #     #     config_dict[fnum] = config_results



    #     # # Chaotic flow, April 2022

    #     # if 'Bilsel' in base_config_dir and 'short' not in base_config_dir:

    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'Bilsel' in base_config_dir and 'short' in base_config_dir:

    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'cytc' in base_config_dir:
    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'cytc_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'cytc_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'cytc_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results


    #     gen_config_results = raw.load_settings(os.path.join(mask_dir, '{}_basic.cfg'.format(mask_prefix)))

    #     for fnum in fnum_list:
    #         # print(fnum)
    #         if os.path.exists(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum))):
    #             config_results = raw.load_settings(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum)))
    #             # print('point config')
    #         else:
    #             config_results = gen_config_results
    #             # print('generic config')

    #         config_dict[fnum] = config_results

    #     print('Processing images')
    #     for name, stuff in diff_list:
    #         print(name)

    #         fnum = int(os.path.splitext(name)[0].split('_')[-1])
    #         # step = name.split('_')[-3]
    #         # ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = config_dict[(fnum, step)]
    #         # raw_settings = config_dict[(fnum, step)]
    #         raw_settings = config_dict[fnum]
    #         # start_point = raw_settings.get('StartPoint')
    #         # end_point = raw_settings.get('EndPoint')

    #         # saxs_raver.doIntegration(output_dir, ai, mask, q_range,
    #         #     maxlen, normlist, do_normalization, calibrate_dict,
    #         #     start_point, end_point, fliplr, flipud,
    #         #     os.path.join(source_dir, name))

    #         a = time.time()
    #         dats, _ = raw.load_and_integrate_images([os.path.join(source_dir,name)], raw_settings)
    #         print(time.time()-a)
    #         data = dats[0]

    #         raw.save_profile(data, settings=raw_settings, datadir=output_dir)

    # except KeyboardInterrupt:
    #     break
