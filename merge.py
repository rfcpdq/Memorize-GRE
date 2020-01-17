# Merge csv files
# https://stackoverflow.com/questions/50885093/how-do-i-remove-rows-with-duplicate-values-of-columns-in-pandas-data-frame
# https://chrisalbon.com/python/data_wrangling/pandas_join_merge_dataframe/


import os
import pandas as pd
from data_utils import file
from config.cfg_parser import paraConfig


class merge(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        # self.col = ["word", "etymonline", "emeaning", "cmeaning"]
        cfg_name = paraConfig().main_cfg()
        self.cfg = paraConfig(cfg_name, section=2).get_cfg()
        self.file_list = self.cfg['file_list']
        self.target_merge = self.cfg['target_merge']
        self.file_list_long = self.cfg['file_list']
        # use working csv as dupl target
        self.cfg2 = paraConfig(cfg_name, section=1).get_cfg()
        self.dupl = self.cfg2['out_name']
        self.target_dupl = self.dupl  # can save output to different csv

    def merge_two(self, file_list=0):
        if file_list == 0:
            file_list = self.file_list
        target = file().load_data(file_list[0])
        temp = file().load_data(file_list[1])
        target = pd.concat([target, temp])
        target = target.drop_duplicates(subset=['word'], keep='first')
        target.to_csv(self.PATH + '/inputs/' + self.target_merge,
                      mode='w', header=True, index=False, encoding='utf-8')
        print('Done!')
        return 0

    def merge_all(self, file_list_long=0):
        if file_list_long == 0:
            file_list = file().list_file()
            print('File to be merged:', file_list)
        else:
            file_list = self.file_list_long
        target = file().load_data(file_list[0])
        for i in range(1, len(file_list)):
            temp = file().load_data(file_list[i])
            target = pd.concat([target, temp])
            target = target.drop_duplicates(subset=['word'], keep='first')
        target.to_csv(self.PATH + '/inputs/' + self.target_merge,
                      mode='w', header=True, index=False, encoding='utf-8')
        print('Done!')
        return 0

    def remove_duplicate(self, dupl=0):
        if dupl == 0:
            dupl = self.dupl
        target = file().load_data(dupl)
        target = target.drop_duplicates(subset=['word'], keep='first')
        target.to_csv(self.PATH + '/inputs/' + self.target_dupl,
                      mode='w', header=True, index=False, encoding='utf-8')
        print('Done!')
        return 0


# merge().merge()
# merge().merge_all()
# merge().remove_duplicate()
