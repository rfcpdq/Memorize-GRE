# Need pass config in future!

# Load
import os
import pandas as pd
from termcolor import cprint
from data_utils import file
from function import func, func2
from tools import adb_func, clear
from config.cfg_parser import paraConfig
from merge import merge


# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Hi There!'))

source = file().load_data()
target = file().empty()


# load config
cfg_name = paraConfig().main_cfg()
print('Default config: ', cfg_name)

cfg = paraConfig(cfg_name, section=1).get_cfg()
out_name = cfg['out_name']
use_adb = cfg['use_adb']
cprint('\n==================================\n', 'magenta')


start = True
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''
    # x = 'politic'

    if x == 'exit':
        target = func(source, target).save_func()
        print(custom_fig.renderText('See You~'))
        start = False
        break

    # ===== edit =====
    # elif x == 'edit':  # have error in saving
    #     source_2 = pd.read_csv(out_name, encoding='utf-8')
    #     temp_target = modify_func(source_2)
    # elif x == 'drop':  # drop last col before saving
    #     target = save_func(target)
    #     source_2 = pd.read_csv(out_name, encoding='utf-8')
    #     source_2 = source_2.drop(source_2.tail(1).index, inplace=True)
    #     source_2.to_csv(out_name, mode='a', header=False, index=False, encoding='utf-8')
    #     cprint('Done!', 'white', 'on_magenta', attrs=['bold'])

    # ===== save / backup =====
    elif x in ['sav', 'sav2']:  # sav2: just save, don't no review
        clear()
        target = func(source, target).save_func()
        # minium review number is 10!
        if x == 'sav':
            source_2 = file().load_data(out_name)
            func2(source_2).rev_custom(1, 10)
        cprint('Save Done!', 'white', 'on_magenta', attrs=['bold'])
        if x == 'sav' and use_adb == True:
            adb_func('next')

    elif x == 'back':
        source_2 = file().load_data(out_name)
        back_name = func(source, target).back_func()
        cprint(back_name, 'Backup Done!', 'white',
               'on_magenta', attrs=['bold'])

    # ===== review (start with '1') =====
    elif x == 'rev':
        clear()
        source_2 = file().load_data(out_name)
        func2(source_2).rev_custom(1, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        clear()
        source_2 = file().load_data(out_name)
        func2(source_2).rev_custom(x.split('-')[-1])
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        clear()
        source_2 = file().load_data(out_name)
        func2(source_2).rev_flashcard(x.split('-')[-1])
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    # ===== adb =====
    elif x in ['n', 'b', 'next', 'next2', '1', '2']:
        adb_func(x)
        cprint('\n')
        continue

    elif x == 'c':
        clear()

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

    elif x == 'merge':
        merge().merge_all()

    else:
        target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
