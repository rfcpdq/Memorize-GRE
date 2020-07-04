# search and uncomment all file().save_rev to save log

# import1
from data_utils import file
from termcolor import cprint

# load config
all_voc = file().load_data()

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
print(custom_fig.renderText("Let's Search!"))

start = True
# file().save_rev(0, 1)
while start:
    cprint('Search word (q to quit):', 'white', 'on_magenta', attrs=['bold'])
    x = input() or ''

    if x in ['exit', 'q']:
        print(custom_fig.renderText("Good Luck :)"))
        start = False
        break

    # ===== clear =====
    elif x == 'c':
        clear()

    elif x == '':
        cprint('Pleace Enter Again!\n', 'red', attrs=['bold'])
        continue

    else:
        # ===== search =====
        func2(all_voc).search(x)

        # ===== online ety =====
        online_ety(x)

    cprint('\n==================================\n', 'magenta')
