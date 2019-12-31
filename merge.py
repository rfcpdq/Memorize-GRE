# Merge csv files
# Just merge B and C for now
# We will merge all data in A.csv and keep updated in future!
# https://stackoverflow.com/questions/50885093/how-do-i-remove-rows-with-duplicate-values-of-columns-in-pandas-data-frame
# https://chrisalbon.com/python/data_wrangling/pandas_join_merge_dataframe/


import os
import pandas as pd
from data_utils import file


class merge(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        self.col = ["word", "etymonline", "emeaning", "cmeaning"]
        self.file_list = ['B.csv', 'C.csv']
        # self.file_list = ['01.csv', '02.csv']  # newer csv at [0]
        self.target_name = 'A.csv'

    def merge(self, file_list=0):
        if file_list == 0:
            file_list = self.file_list
        target = file().load_data(file_list[0])
        temp = file().load_data(file_list[1])
        target = pd.concat([target, temp])
        target = target.drop_duplicates(subset=['word'], keep='first')
        target.to_csv(self.PATH + '/inputs/' + self.target_name,
                      mode='w', header=True, index=False, encoding='utf-8')
        print('Done!')
        return 0


merge().merge()
