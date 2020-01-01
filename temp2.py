import os
import pandas as pd
from cfg_parser import paraConfig
from data_utils import file


class test(paraConfig):
    def __init__(self):
        super().__init__()

    def test(self):
        return self.para


print(test().test())
