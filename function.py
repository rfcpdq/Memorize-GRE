# https://hackernoon.com/4-ways-to-manage-the-configuration-in-python-4623049e841b


import os
import pandas as pd
from termcolor import colored, cprint
from math import ceil
import random
from tools import display, adb_func, clear, modify
from data_utils import file
from config.cfg_parser import paraConfig


class cfg:
    empty = file().empty()
    PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    # load cfg
    cfg_name = paraConfig().main_cfg()
    cfg1 = paraConfig(cfg_name, section=0).get_cfg()
    cfg2 = paraConfig(cfg_name, section=1).get_cfg()
    col = cfg1['col']
    out_name = cfg2['out_name']
    use_adb = cfg2['use_adb']
    back_i = cfg2['back_i']


class func(cfg):
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def def_func(self, x, custom=False):
        if x in self.source.word.values:
            x = self.source.loc[self.source.word == x]
            for col in self.col[1:]:
                print(display(x[col]))
            self.target = self.target.append(x)
            print('\n')
            cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
            if cfg.use_adb == True:
                adb_func('n')
            return self.target
        else:
            temp_li = [x]
            for col in self.col[1:]:
                cprint('Add {} (N to cancel):'.format(col), 'green')
                temp_elem = input() or ''
                if temp_elem == 'n' or temp_elem == 'N':
                    return self.target
                temp_li.append(temp_elem)
            temp_append = pd.DataFrame([temp_li], columns=self.col)
            self.target = self.target.append(temp_append)
            print('\n')
            cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
            if cfg.use_adb == True:
                adb_func('n')
            return self.target

    def save_func(self):
        if len(self.target) == 0:
            return cfg.empty
        else:
            file().save_csv(self.target, cfg.out_name)
            return cfg.empty

    def back_func(self):
        name = 'B_' + str(cfg.back_i) + '.csv'
        file().save_csv(self.target, name)
        cfg.back_i += 1
        return name

        import pdb; pdb.set_trace()  # XXX BREAKPOINT

class func2(cfg):
    def __init__(self, source):
        self.source = source

    def search(self, x):
        if x in self.source.word.values:
            x = self.source.loc[self.source.word == x]
            for col in self.col[1:]:
                print(display(x[col]))
            print('\n')
            # cprint('Find!', 'green', attrs=['bold'])
            return True
        elif x == 'q':
            return False
        else:
            cprint('\nNot Find!', 'green', attrs=['bold'])
            return True

    # custom can be used shuffle r-x review
    def rev_func(self, rev_start, rev_end, banner=True, custom=False):
        if banner == True:
            rev_print = '|| Start: ' + \
                str(rev_start + 1) + '  End: ' + str(rev_end) + ' ||'
            cprint('=' * len(rev_print), 'white', 'on_magenta')
            cprint(rev_print, 'white', 'on_magenta')
            cprint('=' * len(rev_print), 'white', 'on_magenta')
            print('\n')

        li = [i for i in range(rev_start, rev_end)]
        if custom == True:
            random.shuffle(li)
        for i in li:
            x = self.source.iloc[i]
            cprint(x[self.col[0]], 'red', attrs=['bold', 'underline'])
            for col in self.col[1:]:
                print(x[col])

            print('\n')

    def show_position(self, block, rev_prosition, total_len):
        total_rev = ceil(total_len / block)
        rev_prosition = int(rev_prosition)
        part_prosition = '+ Position:' + \
            str(rev_prosition) + '/' + str(total_rev) + ' +'
        print('\n')
        cprint('+' * len(part_prosition), 'green', 'on_grey', attrs=['bold'])
        cprint(part_prosition, 'green', 'on_grey', attrs=['bold'])
        cprint('+' * len(part_prosition), 'green', 'on_grey', attrs=['bold'])
        print('\n')

    def rev_custom(self, rev_prosition, block=60, rand=False):
        # rev 60 words each time, print review precision (12/15)
        # rev_prosition minimum = 1 !!!
        loop = int(block / 10)
        rev_prosition = int(rev_prosition)
        total_len = len(self.source.index)
        self.show_position(block, rev_prosition, total_len)

        total_rev = ceil(total_len / block)
        if rev_prosition != total_rev:
            for i in range(loop):
                part_process = 'Part:' + str(i + 1)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * loop) * 10
                rev_end = rev_start + 10
                if rand == False:
                    self.rev_func(rev_start, rev_end)
                else:
                    self.rev_func(rev_start, rev_end, custom=True)
                cprint('==================================\n', 'magenta')

        else:
            rev_sec_left = ceil(
                (len(self.source.index) - (rev_prosition - 1) * block) / 10)
            for i in range(rev_sec_left - 1):
                part_process = 'Part:' + str(i + 1)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (i + (rev_prosition - 1) * loop) * 10
                rev_end = rev_start + 10
                if rand == False:
                    self.rev_func(rev_start, rev_end)
                else:
                    self.rev_func(rev_start, rev_end, custom=True)
                cprint('==================================\n', 'magenta')

            part_process = 'Part: final'
            cprint(part_process, 'green', attrs=['bold', 'underline'])
            rev_start = (rev_sec_left - 1 + (rev_prosition - 1) * loop) * 10
            rev_end = len(self.source.index)
            if rand == False:
                self.rev_func(rev_start, rev_end)
            else:
                self.rev_func(rev_start, rev_end, custom=True)
            cprint('==================================\n', 'magenta')

    def modify_func(self):
        cprint('Enter word you want to Modify:', 'green', attrs=['bold'])
        x = input()
        if x in self.source.word.values:
            v = self.source.loc[self.source.word == x]
            cprint(display(v[self.col[0]]), 'red', attrs=['bold', 'underline'])
            for col in self.col[1:]:
                print(display(v[col]))
            print('\n')
            
            print(cfg.col)
            mod = input('Modify?(input number to modify specific column)\n') or ''
            if mod == 'n' or mod == 'N':
                return
            elif mod.isnumeric():
                while mod != 'q':
                    mod_col = cfg.col[int(mod)]
                    cprint('\nModify ' + mod_col + ' as:', 'red', attrs=['bold', 'underline'])
                    temp_str = modify(str(v[mod_col].values[0]))
                    print(repr(temp_str))
                    confirm_mod = input('Confirm? (n to reinput, q to exit)\n') or ''
                    if confirm_mod == 'n' or confirm_mod == 'N':
                        return
                    elif confirm_mod == 'q':
                        return
                    else:
                        self.source.loc[self.source.word == x, mod_col] = temp_str
                        csv_dir = '/inputs/'
                        self.source.to_csv(cfg.PATH + csv_dir + cfg.out_name, index=False, encoding='utf-8')
                        cprint('Done!', 'white', 'on_magenta', attrs=['bold'])
                        return
            else:
                print('wrong input!')

    def rev_flashcard(self, rev_prosition, block=30, flashcard=1, rand=False):
        # rev '30' words each time, print review precision (12/15)
        # flashcard shows 1 word by default
        # rev_prosition minimum = 1 !!!
        rev_prosition = int(rev_prosition)
        total_len = len(self.source.index)
        # self.show_position(block, rev_prosition, total_len)

        total_rev = ceil(total_len / block)
        if rev_prosition != total_rev:
            i = 0
            mark_list = ['nan'] * int(block)
            li = [i for i in range(0, block)]
            if rand == True:
                random.shuffle(li)
            while i < block:
                clear()
                part_process = 'Prosition:' + str(i + 1) + '/' + str(block)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (li[i] + (rev_prosition - 1) * block) * flashcard
                rev_end = rev_start + flashcard
                self.rev_func(rev_start, rev_end, False)
                x = input('Enter / j / k to move, q to cancel\n') or ''
                if x == 'k':
                    i -= 1
                elif x == 'q':
                    break
                elif x == 'm':
                    # update_remember(self.source, rev_start)
                    if pd.isnull(self.source.iloc[-(rev_start + 1)].remember) == True:
                        mark_list[i] = 1
                    else:
                        mark_list[i] = int(
                            self.source.iloc[-(rev_start + 1)].remember + 1)
                    i += 1
                else:
                    i += 1
                cprint('==================================\n', 'magenta')
            # https://stackoverflow.com/questions/45093241/how-to-replace-part-of-dataframe-in-pandas

            # print(mark_list)
            # # self.source = file().load_data(cfg.out_name)
            # start = (rev_prosition - 1) * block * flashcard + 1
            # end = (rev_prosition) * block * flashcard + 1
            # # x = self.source.word.iloc[-start]
            # # print(display(self.source.loc[self.source.word == x].word))
            # self.source.remember.values[-start: -end] = mark_list
            # # self.source.iloc[-start: -end].remember = mark_list

            # empty = file().empty()
            # func(self.source, empty).save_func()

        else:
            rev_sec_left = total_len - (rev_prosition - 1) * block
            i = 0
            li = [i for i in range(0, rev_sec_left)]
            if rand == True:
                random.shuffle(li)
            while i < rev_sec_left:
                clear()
                part_process = 'Prosition:' + \
                    str(i + 1) + '/' + str(rev_sec_left)
                cprint(part_process, 'green', attrs=['bold', 'underline'])
                rev_start = (li[i] + (rev_prosition - 1) * block) * flashcard
                rev_end = rev_start + flashcard
                self.rev_func(rev_start, rev_end, False)
                x = input('Enter / j / k to move, q to cancel\n') or ''
                if x == 'k':
                    i -= 1
                elif x == 'q':
                    break
                elif x == 'm':
                    # update_remember(self.source, rev_start)
                    if pd.isnull(self.source.iloc[-(rev_start + 1)].remember) == True:
                        mark_list[i] = 1
                    else:
                        mark_list[i] = int(
                            self.source.iloc[-(rev_start + 1)].remember + 1)
                    i += 1
                else:
                    i += 1
                cprint('==================================\n', 'magenta')

