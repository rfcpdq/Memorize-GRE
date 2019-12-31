# Need pass config in future!

# Load
import os
import pandas as pd
from termcolor import cprint
from data_utils import file
from function import func, func2
from tools import adb_func, clear

# Greeting
from pyfiglet import Figlet
custom_fig = Figlet(font='contessa')  # italic / contessa / basic
print(custom_fig.renderText('Hi There!'))


source = file().load_data()
target = file().empty()


start = True
while start:
    cprint('Enter Word/Function Name:', 'green', attrs=['bold'])
    x = input() or ''
    # x = 'politic'

    if x == 'exit':
        x = 'sav'
        print(custom_fig.renderText('See You~'))
        start = False
        break

    # ===== edit =====
    # elif x == 'edit':  # have error in saving
    #     source_2 = pd.read_csv('B.csv', encoding='utf-8')
    #     temp_target = modify_func(source_2)
    # elif x == 'drop':  # drop last col before saving
    #     target = save_func(target)
    #     source_2 = pd.read_csv('B.csv', encoding='utf-8')
    #     source_2 = source_2.drop(source_2.tail(1).index, inplace=True)
    #     source_2.to_csv('B.csv', mode='a', header=False, index=False, encoding='utf-8')
    #     cprint('Done!', 'white', 'on_magenta', attrs=['bold'])

    # ===== save / backup =====
    elif x in ['save', 'sav']:
        clear()
        target = func(source, target).save_func()
        source_2 = file().load_data('B.csv')
        func2(source_2).rev_func(0, 10)
        cprint('Save Done!', 'white', 'on_magenta', attrs=['bold'])
        if x == 'sav':
            adb_func('next')

    elif x == 'back':
        source_2 = file().load_data('B.csv')
        back_name = func(source, target).back_func()
        cprint(back_name, 'Backup Done!', 'white',
               'on_magenta', attrs=['bold'])

    # ===== review =====
    elif x == 'rev':
        clear()
        source_2 = file().load_data('B.csv')
        func2(source_2).rev_func(0, 10)
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'r-':
        clear()
        source_2 = file().load_data('B.csv')
        func2(source_2).rev_custom(x.split('-')[-1])
        cprint('Rev Done!', 'white', 'on_magenta', attrs=['bold'])

    elif x[:2] == 'f-':
        clear()
        source_2 = file().load_data('B.csv')
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

    else:
        target = func(source, target).def_func(x)

    cprint('\n==================================\n', 'magenta')
