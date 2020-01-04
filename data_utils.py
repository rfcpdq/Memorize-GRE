# Load config in the future

import os
import pandas as pd
from config.cfg_parser import paraConfig


class file(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        # load cfg
        cfg_name = paraConfig().main_cfg()
        self.cfg = paraConfig(cfg_name, section=0).get_cfg()
        self.col = self.cfg['col']
        self.default_name = self.cfg['default_name']
        # print(self.default_name)

    def load_data(self, name=0):
        if name == 0:
            name = self.default_name
        source = pd.read_csv(self.PATH + '/inputs/' +
                             name, encoding='utf-8')
        return source

    def save_csv(self, target, out_name):
        target.to_csv(self.PATH + '/inputs/' + out_name,
                      mode='a', header=False, index=False, encoding='utf-8')

    def empty(self):
        empty = pd.DataFrame(columns=self.col)
        return empty

    def list_file(self):
        file_list = []
        for file in os.listdir('./inputs'):
            if file != self.default_name and file[-3:] == 'csv':
                file_list.append(file)
        return file_list

    def list_csv(self):
        file_list = []
        for file in os.listdir():
            if file != 'config_main.cfg' and file[-3:] == 'cfg':
                file_list.append(file)
        return file_list

# print(file().list_file())
# print(file().list_csv())
