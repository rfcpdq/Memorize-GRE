import os
import pandas as pd
from termcolor import colored, cprint
from math import ceil
from tools import display, adb_func
from data_utils import file
from config.cfg_parser import paraConfig


class func(object):
    def __init__(self, source, target):
        self.source = source
        self.target = target
        self.empty = file().empty()
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        # load cfg
        cfg_name = paraConfig().main_cfg()
        self.cfg1 = paraConfig(cfg_name, section=0).get_cfg()
        self.cfg2 = paraConfig(cfg_name, section=1).get_cfg()
        self.col = self.cfg1['col']
        self.out_name = self.cfg2['out_name']
        self.use_adb = self.cfg2['use_adb']
        self.back_i = self.cfg2['back_i']

    def def_func(self, x, custom=False):
        if x in self.source.word.values:
            print(display(self.source.loc[self.source.word == x].etymonline))
            print(display(self.source.loc[self.source.word == x].emeaning))
            print(display(self.source.loc[self.source.word == x].cmeaning))
            self.target = self.target.append(
                self.source.loc[self.source.word == x])
            print('\n')
            cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
            if self.use_adb == True:
                adb_func('n')
            return self.target
        else:
            cprint('Add etymonline (N to cancel):', 'green')
            ety = input() or ''
            if ety == 'n' or ety == 'N':
                return self.target
            cprint('Add e_meaning (c to add c_meaning):', 'green')
            em = input() or ''
            if em == 'c':
                em = ''
                # em = input('Add e_meaning:\n') or ''
                cprint('Add c_meaning:', 'green')
                cm = input() or ''
            else:
                cm = ''
            # print(x, ety, em, cm)
            self.target = self.target.append(
                {"word": x, "etymonline": ety, "emeaning": em, "cmeaning": cm}, ignore_index=True)
            print('\n')
            cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
            if self.use_adb == True:
                adb_func('n')
            return self.target

    # def modify_func(self, x):
    #     x = input('Enter word you want to Modify:\n')
    #     if x in self.source.word.values:
    #         print(self.source.loc[self.source.word == x].word)
    #         print(self.source.loc[self.source.word == x].etymonline)
    #         print(self.source.loc[self.source.word == x].emeaning)
    #         print(self.source.loc[self.source.word == x].cmeaning)

    #     modify = input('Modify?\n') or 'n'
    #     if modify == 'n' or modify == 'N':
    #         return self.source
    #     else:
    #         print('Modify description:\n')
    #         print(self.source.loc[self.source.word == x].etymonline)
    #         ety = input('Modify etymonline:\n') or self.source.loc[self.source.word == x].etymonline
    #         print(self.source.loc[self.source.word == x].emeaning)
    #         em = input('Modify e_meaning:\n') or self.source.loc[self.source.word == x].emeaning
    #         cm = self.source.loc[self.source.word == x].cmeaning
    #         self.source.loc[self.source.word == x, ["word", "etymonline", "emeaning", "cmeaning"]] = [x, ety, em, cm]
    #         print('\n\n')
    #         cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
    #         return self.source

    def save_func(self):
        if len(self.target) == 0:
            return self.empty
        else:
            file().save_csv(self.target, self.out_name)
            return self.empty

    def back_func(self):
        name = 'B_' + str(self.back_i) + '.csv'
        file().save_csv(self.target, name)
        self.back_i += 1
        return name


class func2(object):
    def __init__(self, source):
        self.source = source
        self.total_len = len(source.index)

    def rev_func(self, rev_start, rev_end, banner=True, custom=False):
        if banner == True:
            rev_print = '|| Start: ' + \
                str(rev_start + 1) + '  End: ' + str(rev_end) + ' ||'
            cprint('=' * len(rev_print), 'white', 'on_magenta')
            cprint(rev_print, 'white', 'on_magenta')
            cprint('=' * len(rev_print), 'white', 'on_magenta')
            print('\n')

        for i in range(rev_start + 1, rev_end + 1):
            x = self.source.word.iloc[-i]
            if x in self.source.word.values and custom == False:
                cprint(display(self.source.loc[self.source.word == x].word), 'red', attrs=[
                       'bold', 'underline'])
                print(
                    display(self.source.loc[self.source.word == x].etymonline))
                print(
                    display(self.source.loc[self.source.word == x].emeaning))
                print(
                    display(self.source.loc[self.source.word == x].cmeaning))
                print('\n')

    def show_position(self, block, rev_prosition):
        total_rev = ceil(self.total_len / block)
        rev_prosition = int(rev_prosition)
        part_prosition = '+ Position:' + \
            str(rev_prosition) + '/' + str(total_rev) + ' +'
        print('\n')
        cprint('+' * len(part_prosition), 'green', 'on_grey', attrs=['bold'])
        cprint(part_prosition, 'green', 'on_grey', attrs=['bold'])
        cprint('+' * len(part_prosition), 'green', 'on_grey', attrs=['bold'])
        print('\n')

    def rev_custom(self, rev_prosition, block=60):
        # rev 60 words each time, print review precision (12/15)
        # rev_prosition minimum = 1 !!!
        loop = int(block / 10)
        rev_prosition = int(rev_prosition)
        self.show_position(block, rev_prosition)

        total_rev = ceil(self.total_len / block)
        if rev_prosition != total_rev:
            for i in range(loop):
                part_process = 'Part:' + str(i + 1)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * loop) * 10
                rev_end = rev_start + 10
                self.rev_func(rev_start, rev_end)
                cprint('==================================\n', 'magenta')

        else:
            rev_sec_left = ceil(
                (len(self.source.index) - (rev_prosition - 1) * block) / 10)
            for i in range(rev_sec_left - 1):
                part_process = 'Part:' + str(i + 1)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * loop) * 10
                rev_end = rev_start + 10
                self.rev_func(rev_start, rev_end)
                cprint('==================================\n', 'magenta')

            part_process = 'Part: final'
            cprint(part_process, 'green', attrs=['bold', 'underline'])
            rev_start = (rev_sec_left - 1 + (rev_prosition - 1) * loop) * 10
            rev_end = len(self.source.index)
            self.rev_func(rev_start, rev_end)
            cprint('==================================\n', 'magenta')

    def rev_flashcard(self, rev_prosition, block=30, flashcard=1):
        # rev '30' words each time, print review precision (12/15)
        # flashcard shows 1 word by default
        # rev_prosition minimum = 1 !!!
        rev_prosition = int(rev_prosition)
        self.show_position(block, rev_prosition)

        total_rev = ceil(self.total_len / block)
        if rev_prosition != total_rev:
            for i in range(block):
                part_process = 'Prosition:' + str(i + 1) + '/' + str(block)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * block) * flashcard
                rev_end = rev_start + flashcard
                self.rev_func(rev_start, rev_end, False)
                x = input('Press Enter to Continue')
                cprint('==================================\n', 'magenta')

        else:
            rev_sec_left = self.total_len - (rev_prosition - 1) * block
            for i in range(rev_sec_left):
                part_process = 'Prosition:' + \
                    str(i + 1) + '/' + str(rev_sec_left)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * block) * flashcard
                rev_end = rev_start + flashcard
                self.rev_func(rev_start, rev_end, False)
                x = input('Press Enter to Continue')
                cprint('==================================\n', 'magenta')
