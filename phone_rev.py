# can't auto clear in pydroid3
# Use different log file
# No func().def_func()
# Block size for review = 30

# import1
from config.cfg_parser import update_cfg
from data_utils import file
from config.cfg_parser import paraConfig
from termcolor import cprint


# Choose Config
update_cfg().change_main_cfg()

source = file().load_data()
target = file().empty()
cfg_name = paraConfig().main_cfg()

cfg_func = paraConfig(cfg_name, section=1).get_cfg()
out_name = cfg_func['out_name']
use_adb = cfg_func['use_adb']
cfg_merge = paraConfig(cfg_name, section=2).get_cfg()
target_merge = cfg_merge['target_merge']  # All.csv
cprint('\n==================================\n', 'magenta')


# import2 - phone
import os
from os import system, name
import pandas as pd
from function import func2, func3


# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Let\'s go!'))


start = True
file().save_rev(0, 1, phone=True)

start = True
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''
    # x = 'politic'

    if x == 'exit':
        print(custom_fig.renderText('See You~'))
        start = False
        break

    # ===== review =====
    elif x == 'rev':
        system('clear')
        source_2 = file().load_data(out_name)
        func2(source_2).rev_custom(1, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        source_2 = file().load_data(out_name)
        rev = x.split('-')[-1]
        func2(source_2).rev_custom(rev, 30)
        file().save_rev(rev, phone=True)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        source_2 = file().load_data(out_name)
        rev = x.split('-')[-1]
        func3().rev_flashcard(source_2, rev, 30)
        file().save_rev(rev, phone=True)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x == 'c':
        system('clear')

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

    # else:
    #     target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
