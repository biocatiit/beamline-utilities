import os
import glob

os.sys.path.append(os.path.abspath('../pyfai_integration/'))
import saxs_raver

#March 2019

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, output_dir]
# Note that if fprefix is None, all files in the directory will be processed

batch_list = [
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/native_buffer1/',
    # 'native_buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/native_buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/native_cytc1/',
    # 'native_cytc1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/native_cytc1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer1/',
    # 'buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc1/',
    # 'cytc1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc2/',
    # 'cytc2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc3/',
    # 'cytc3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water7/',
    # 'water7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water8/',
    # 'water8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water9/',
    # 'water9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer4/',
    # 'buffer4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc4/',
    # 'cytc4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc5/',
    # 'cytc5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer5/',
    # 'buffer5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water15/',
    # 'water15',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water15'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water16/',
    # 'water16',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water16'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub1/',
    # 'ub1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub2/',
    # 'ub2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub3/',
    # 'ub3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer4/',
    # 'buffer4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub4/',
    # 'ub4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer5/',
    # 'buffer5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer6/',
    # 'buffer6',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer6'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub5/',
    # 'ub5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer7/',
    # 'buffer7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub6/',
    # 'ub6',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub6'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub7/',
    # 'ub7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer8/',
    # 'buffer8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub8/',
    # 'ub8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub9/',
    # 'ub9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer9/',
    # 'buffer9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub10/',
    # 'ub10',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub10'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub11/',
    # 'ub11',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub11'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub12/',
    # 'ub12',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub12'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/buffer1/',
    # 'buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt1/',
    # 'twt1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt1/',
    # 'tmt1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt2/',
    # 'tmt2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt2/',
    # 'twt2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt3/',
    # 'twt3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt3/',
    # 'tmt3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em1/',
    # 'em1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em2/',
    # 'em2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em2'
    # ],
    ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer4/',
    'buffer4',
    '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer4'
    ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer1_PEG/',
    # 'buffer1_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer1_PEG'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em1_PEG/',
    # 'em1_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em1_PEG'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em2_PEG/',
    # 'em2_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em2_PEG'
    # ],
]

base_config_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing'

# ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = saxs_raver.init_integration(cfg_file)

# start_point = raw_settings.get('StartPoint')
# end_point = raw_settings.get('EndPoint')


for source_dir, fprefix, output_dir in batch_list:
    print fprefix

    try:
        old_dir_list_dict = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print 'Getting file list'
        diff_list, old_dir_list_dict = saxs_raver.getNewFiles(source_dir, old_dir_list_dict, fprefix)

        print 'Loading config files'
        f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_*.tif'.format(fprefix)))
        fnum_list = [int(fname.split('_')[-1].strip('.tif')) for fname in f_list]
        fnum_list.sort()

        config_dict = {}

        if 'martin' in source_dir:
            gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_basic.cfg'))
            for fnum in fnum_list:
                if os.path.exists(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum))):
                    config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum)))
                else:
                    config_results = gen_config_results

                config_dict[fnum] = config_results

        elif 'pinto' in source_dir:
            gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_basic.cfg'))
            for fnum in fnum_list:
                if os.path.exists(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum))):
                    config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum)))
                else:
                    config_results = gen_config_results

                config_dict[fnum] = config_results

        elif 'sosnick' in source_dir:
            if len(fnum_list) == 30:
                prefix='short'
            else:
                prefix='long'

            gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_basic.cfg'.format(prefix)))
            for fnum in fnum_list:
                if os.path.exists(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum))):
                    config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum)))
                else:
                    config_results = gen_config_results

                config_dict[fnum] = config_results

        elif 'cytc' in source_dir:
            if fprefix in ['native_cytc1', 'native_buffer1']:
                prefix = 'native'
            elif fprefix in ['buffer2', 'buffer3', 'cytc2', 'cytc3']:
                prefix = '0808'
            elif fprefix in ['buffer4' , 'buffer5', 'cytc4', 'cytc5']:
                prefix = '0809'

            gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_basic.cfg'.format(prefix)))

            for fnum in fnum_list:
                if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum))):
                    config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum)))
                else:
                    config_results = gen_config_results

                config_dict[fnum] = config_results


        print 'Processing images'
        for name, stuff in diff_list:
            print name

            fnum = int(name.split('_')[-1].strip('.tif'))
            ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = config_dict[fnum]
            start_point = raw_settings.get('StartPoint')
            end_point = raw_settings.get('EndPoint')

            saxs_raver.doIntegration(output_dir, ai, mask, q_range,
                maxlen, normlist, do_normalization, calibrate_dict,
                start_point, end_point, fliplr, flipud,
                os.path.join(source_dir, name))

    except KeyboardInterrupt:
        break
