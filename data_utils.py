# Load config in the future

import os
import pandas as pd
from config.cfg_parser import paraConfig
from time import gmtime, strftime


class file(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        # load cfg
        self.cfg_name = paraConfig().main_cfg()
        self.cfg = paraConfig(self.cfg_name, section=0).get_cfg()
        self.col = self.cfg['col']
        self.default_name = self.cfg['default_name']
        # print(self.default_name)

    def load_data(self, name=0, folder=1):
        if name == 0:
            name = self.default_name
        csv_dir = '/inputs/'
        if folder != 1:
            csv_dir = csv_dir + str(folder)
        source = pd.read_csv(self.PATH + csv_dir +
                             name, encoding='utf-8')
        return source

    def save_csv(self, target, out_name, folder=1):
        csv_dir = '/inputs/'
        if folder != 1:
            csv_dir = csv_dir + str(folder)
        target.to_csv(self.PATH + csv_dir + out_name,
                      mode='a', header=False, index=False, encoding='utf-8')

    def save_rev(self, rev, time=0, phone=False):
        csv_dir = '/oth/'
        if phone == True:
            f = open(self.PATH + csv_dir + "log_phone.txt", "a")
        else:
            f = open(self.PATH + csv_dir + "log.txt", "a")
        if time == 1:
            time = strftime("%a, %d %b %Y %H:%M", gmtime())
            f.write('\n' + self.cfg_name + '\n')
            f.write(time + '\n')
            f.write("==========\n")
        else:
            f.write(rev + '\n')
        f.close()

    def empty(self):
        empty = pd.DataFrame(columns=self.col)
        return empty

    def list_file(self, folder=1):
        file_list = []
        csv_dir = '../inputs'
        if folder != 1:  # folder=1 => inputs2
            csv_dir = csv_dir + str(folder)
        for file in os.listdir(csv_dir):
            if file != self.default_name and file[-3:] == 'csv':
                file_list.append(file)
        return file_list
