# Load config in the future

import os
import pandas as pd


class file(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        self.col = ["word", "etymonline", "emeaning", "cmeaning"]
        self.default_name = 'C.csv'  # default file to be open

    # def load_cfg(self):
    #     return default_name

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
        for file in os.listdir():
            if file[0] != 'A' and file[-3:] == 'csv':
                file_list.append(file)
        return file_list
