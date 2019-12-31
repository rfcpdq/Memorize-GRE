import os
import time
import configparser


class MyConfigParser(configparser.ConfigParser):
    def __init__(self, defaults=None):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, optionstr):
        return optionstr


class paraConfig(object):
    def __init__(self, conf_f='config.cfg', updatePara={}):
        self.cp = MyConfigParser()
        # print("Loading config file:", conf_f, ".................")
        self.cp.read(conf_f)
        self.para = dict()
        self.updatePara = updatePara

        for sec in self.cp.sections():
            # print("\n[%s]\n" % sec)
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

    def removeFileInFirstDir(self, targetDir):
        for file in os.listdir(targetDir):
            targetFile = os.path.join(targetDir, file)
            if os.path.isfile(targetFile):
                os.remove(targetFile)


# print(paraConfig().get_cfg())
