import os
import time
import configparser


class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class paraConfig(object):
    def __init__(self, conf_f='config_A.cfg', section=0, updatePara={}):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        self.cp = MyConfigParser()
        # print("Loading config file:", conf_f, ".................")
        self.cp.read(conf_f)
        self.para = dict()
        self.updatePara = updatePara

        # for sec in self.cp.sections():
        sec = self.cp.sections()[section]
        # print('Sec:', sec, self.cp.sections()[0])
        for opt, opt_type_value in self.cp.items(sec):
            opt_type, opt_value = opt_type_value.split(':', 1)
            if opt in self.updatePara:
                opt_value = self.updatePara[opt]
            if opt_type == 'str':
                self.para[opt] = opt_value.strip()
            elif opt_type == 'int':
                self.para[opt] = int(opt_value)
            elif opt_type == 'float':
                self.para[opt] = float(opt_value)
            elif opt_type == 'int_list':
                self.para[opt] = eval(opt_value)
            elif opt_type == 'float_list':
                self.para[opt] = eval(opt_value)
            elif opt_type == 'list':
                self.para[opt] = eval(opt_value)
            elif opt_type == 'bool':
                self.para[opt] = True if opt_value.strip(
                ) == 'True' else False
            elif opt_type == 'str_eval':
                self.para[opt] = eval(opt_value)
            elif opt_type == 'NoneType':
                self.para[opt] = None
            else:
                raise ValueError('Wrong type option')
            # if self.para[opt] is None:
            #     print(opt, "= None")
            # else:
            #     print(opt, "=", self.para[opt])

    def get_cfg(self):
        return self.para

    def main_cfg(self):
        self.cfg = paraConfig('config_main.cfg').get_cfg()
        self.cfg_name = self.cfg['cfg_name']
        return self.cfg_name


# print(paraConfig().main_cfg())
