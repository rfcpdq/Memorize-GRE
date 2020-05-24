# Use different log file
# No func().def_func()
# Block size for review = 30

# import1
from config.cfg_parser import update_cfg
from data_utils import file
from config.cfg_parser import paraConfig
from termcolor import cprint
from tools import clear


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


# import2 - phone
import os
from os import system, name
import pandas as pd
from function import func2


# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Let\'s go!'))


start = True
# file().save_rev(0, 1, phone=True)

start = True
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''
    # x = 'politic'

    if x in ['exit', 'q']:
        print(custom_fig.renderText('See You~'))
        start = False
        break

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
            cprint('Search word (q to quit):', 'white',
                   'on_magenta', attrs=['bold'])
            y = input() or ''
            # target_csv = file().load_data(target_merge)
            insrch = func2(all_voc).search(y)

    # ===== review (start with '1') =====
    elif x == 'rev':
        clear()
        target_csv = file().load_data(target_csv_name)
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

    # ===== other =====
    elif x == 'c':
        system('clear')

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

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

    # else:
    #     target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
