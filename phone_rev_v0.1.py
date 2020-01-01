# can not auto clear

# Load
import os
from os import system, name
import pandas as pd
from termcolor import cprint
from data_utils import file
from function import func2
from tools import clear

# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Hi There!'))


source = file().load_data()
# target = file().empty()
source_2 = file().load_data('B.csv')


start = True
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''
    # x = 'politic'

    if x == 'exit':
        print(custom_fig.renderText('See You~'))
        start = False
        break

    # # ===== save / backup =====
    # elif x in ['save', 'sav']:
    #     clear()
    #     target = func(source, target).save_func()
    #     source_2 = file().load_data('B.csv')
    #     func2().rev_func(source_2, 0, 10)
    #     cprint('Save Done!', 'white', 'on_magenta', attrs=['bold'])

    # elif x == 'back':
    #     source_2 = file().load_data('B.csv')
    #     back_name = func(source, target).back_func()
    #     cprint(back_name, 'Backup Done!', 'white',
    #            'on_magenta', attrs=['bold'])

    # ===== review =====
    elif x == 'r':
        system('clear')
        func2().rev_func(source_2, 0, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        clear()
        source_2 = file().load_data('B.csv')
        func2(source_2).rev_custom(x.split('-')[-1], 30)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        clear()
        source_2 = file().load_data('B.csv')
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
