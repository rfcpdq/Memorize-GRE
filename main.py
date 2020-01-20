# import1
from config.cfg_parser import update_cfg
from data_utils import file
from config.cfg_parser import paraConfig
from termcolor import cprint


# Choose Config
update_cfg().change_main_cfg()

source = file().load_data()
target = file().empty()  # buffer
cfg_name = paraConfig().main_cfg()

cfg_func = paraConfig(cfg_name, section=1).get_cfg()
out_name = cfg_func['out_name']
use_adb = cfg_func['use_adb']
cfg_merge = paraConfig(cfg_name, section=2).get_cfg()
target_merge = cfg_merge['target_merge']  # All.csv
cprint('\n==================================\n', 'magenta')


# import2
import os
import pandas as pd
from function import func, func2, func3
from tools import adb_func, clear
from merge import merge


# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Hi There!'))


start = True
file().save_rev(0, 1)
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''

    if x == 'exit':
        target = func(source, target).save_func()
        print(custom_fig.renderText('See You~'))
        start = False
        break

    # ===== edit =====
    # elif x == 'edit':  # have error in saving
    #     source_2 = pd.read_csv(out_name, encoding='utf-8')
    #     temp_target = modify_func(source_2)

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

    elif x == 'bk':
        source_2 = file().load_data(out_name)
        back_name = func(source, target).back_func()
        cprint(back_name, 'Backup Done!', 'white',
               'on_magenta', attrs=['bold'])

    elif x == 'srch':
        insrch = True
        while insrch:
            cprint('Search word (q to quit):', 'white',
                   'on_magenta', attrs=['bold'])
            y = input() or ''
            source_2 = file().load_data(target_merge)
            insrch = func2(source_2).search(y)

    # ===== review (start with '1') =====
    elif x == 'rev':
        clear()
        source_2 = file().load_data(out_name)
        func2(source_2).rev_custom(0, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        clear()
        source_2 = file().load_data(out_name)
        rev = x.split('-')[-1]
        func2(source_2).rev_custom(rev)
        file().save_rev(rev)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        clear()
        source_2 = file().load_data(out_name)
        rev = x.split('-')[-1]
        func3().rev_flashcard(source_2, rev)
        file().save_rev(rev)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    # ===== adb =====
    elif x in ['n', 'b', 'next', 'next2', 'p', '1', '2']:
        adb_func(x)
        cprint('\n')
        continue

    # ===== clear =====
    elif x == 'c':
        clear()

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

    # ===== merge =====
    elif x == 'merge':
        merge().merge_all()
    
    # elif x == 'merge2':
    #     merge().merge_two()

    elif x == 'dupl':
        merge().remove_duplicate()

    # ===== other =====
    elif x == 'len':
        source_2 = file().load_data(out_name)
        print('Length: ', len(source_2.index))

    # ===== def =====
    else:
        target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
