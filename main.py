# search and uncomment all file().save_rev to save log

# import1
from data_utils import file
from config.cfg_parser import update_cfg
from config.cfg_parser import paraConfig
from termcolor import cprint

# load config
all_voc = file().load_data()  # All.csv
buffer_df = file().empty()  # buffer
cfg_name = paraConfig().main_cfg()

cfg_func = paraConfig(cfg_name, section=1).get_cfg()
target_csv_name = cfg_func['out_name']  # target csv
use_adb = cfg_func['use_adb']

csv_print = '|| Cfg file: ' + \
    cfg_name + ' ||'

print('\n')
print('=' * len(csv_print))
print(csv_print)
print('=' * len(csv_print))

cprint('\n==================================\n', 'magenta')

# import2
import os
import pandas as pd
from function import func, func2
from tools import adb_func, clear
from merge import merge
from ety import online_ety

# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText("Let's Go!"))

start = True
# file().save_rev(0, 1)
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''

    if x == 'exit':
        buffer_df = func(all_voc, buffer_df).save_func()
        print(custom_fig.renderText("See You :)"))
        start = False
        break

    if x == 'q':
        print(custom_fig.renderText("See You :)"))
        start = False
        break

    # ===== edit =====
    # elif x == 'e-':
    elif x == 'e':
        target_csv = file().load_data(target_csv_name)
        func2(target_csv).modify_func()

    # ===== save / backup =====
    elif x in ['sav', 'sav2']:  # sav2: just save, don't no review
        clear()
        buffer_df = func(all_voc, buffer_df).save_func()
        # minium review number is 10!
        if x == 'sav':
            target_csv = file().load_data(target_csv_name)
            func2(target_csv).rev_custom(0, 10)
        cprint('Save Done!', 'white', 'on_magenta', attrs=['bold'])

        if x == 'sav' and use_adb == True:
            adb_func('next')

    elif x == 'bk':
        target_csv = file().load_data(target_csv_name)
        back_name = func(all_voc, buffer_df).back_func()
        cprint(back_name,
               'Backup Done!',
               'white',
               'on_magenta',
               attrs=['bold'])

    # ===== search =====
    # check if xxx is in current csv
    elif x[:2] == 's-':
        target_csv = file().load_data(target_csv_name)
        y = x.split('-')[-1]
        func2(target_csv).search(y)
        # file().save_rev(rev)
        cprint('Search Done!', 'white', 'on_magenta', attrs=['bold'])

    # search in all csv
    elif x == 'ss':
        insrch = True
        while insrch:
            cprint('Search word (q to quit):',
                   'white',
                   'on_magenta',
                   attrs=['bold'])
            y = input() or ''
            # target_csv = file().load_data(target_merge)
            insrch = func2(all_voc).search(y)

    # ===== online ety =====
    elif x == 'ety':
        insrch = True
        while insrch:
            cprint('Search word (q to quit):',
                   'white',
                   'on_magenta',
                   attrs=['bold'])
            y = input() or ''
            if y == 'q':
                insrch = False
            else:
                online_ety(y)

    # ===== review (start with '1') =====
    elif x == 'rev':
        clear()
        target_csv = file().load_data(target_csv_name)
        if len(target_csv.index) < 10:
            print('Less than 10 values')
            func2(target_csv).rev_custom(1, 10)
        else:
            func2(target_csv).rev_custom(0, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        clear()
        target_csv = file().load_data(target_csv_name)
        rev = x.split('-')[-1]
        func2(target_csv).rev_custom(rev, 30)
        # file().save_rev(rev)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:3] == 'rr-':
        clear()
        target_csv = file().load_data(target_csv_name)
        rev = x.split('-')[-1]
        func2(target_csv).rev_custom(rev, 30, rand=True)
        # file().save_rev(rev)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        clear()
        target_csv = file().load_data(target_csv_name)
        rev = x.split('-')[-1]
        func2(target_csv).rev_flashcard(rev, 30)
        # file().save_rev(rev)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:3] == 'rf-':
        clear()
        target_csv = file().load_data(target_csv_name)
        rev = x.split('-')[-1]
        func2(target_csv).rev_flashcard(rev, 30, rand=True)
        # file().save_rev(rev)
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
        # cfg_merge = paraConfig(cfg_name, section=2).get_cfg()
        # target_merge = cfg_merge['target_merge']  # All.csv
        merge().merge_all()

    # elif x == 'merge2':
    #     merge().merge_two()

    elif x == 'dupl':
        merge().remove_duplicate()

    # ===== other =====
    elif x == 'len':
        target_csv = file().load_data(target_csv_name)
        print('Length: ', len(target_csv.index))

    elif x == 'cfg':
        update_cfg().change_main_cfg()

        all_voc = file().load_data()
        buffer_df = file().empty()  # buffer
        cfg_name = paraConfig().main_cfg()

        cfg_func = paraConfig(cfg_name, section=1).get_cfg()
        target_csv_name = cfg_func['out_name']
        use_adb = cfg_func['use_adb']
        # cfg_merge = paraConfig(cfg_name, section=2).get_cfg()
        # target_merge = cfg_merge['target_merge']  # All.csv
        cprint('\n==================================\n', 'magenta')
        print(custom_fig.renderText("Please Restart :)"))
        start = False
        break

    # ===== def =====
    else:
        buffer_df = func(all_voc, buffer_df).def_func(x)

    cprint('\n==================================\n', 'magenta')
