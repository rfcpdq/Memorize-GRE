# can not auto clear

# Load
import os
from os import system, name
import pandas as pd
from termcolor import cprint
from data_utils import file
from function import func2
from config.cfg_parser import paraConfig


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
        system('clear')
        source_2 = file().load_data(out_name)
        func2(source_2).rev_custom(x.split('-')[-1])
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        system('clear')
        source_2 = file().load_data(out_name)
        func2(source_2).rev_flashcard(x.split('-')[-1])
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x == 'c':
        system('clear')

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

    # else:
    #     target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
