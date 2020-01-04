import os
import pandas as pd
from config.cfg_parser import paraConfig
from data_utils import file


class test(object):
    def __init__(self):
        self.cfg = paraConfig(section=0).get_cfg()
        self.col = self.cfg['col']

    def test(self):
        return self.col

    def test2(self):
        return self.cfg


print(test().test())
