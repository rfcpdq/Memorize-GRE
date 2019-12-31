import os
import pandas as pd
from textblob import Word
from data_utils import file
from tools import display


PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
os.chdir(PATH)
source = pd.read_csv(PATH + '/inputs/' +
                     'B_.csv', names=['word', 'emeaning_old', 'emeaning_new'], encoding='utf-8')
source.word = source.word.apply(lambda x: x.split(' ')[-1])
source.word = source.word.apply(lambda x: x.split('\n')[0])

source.to_csv(PATH + '/inputs/' + 'B_.csv',
              mode='w', header=False, index=False, encoding='utf-8')

print('Done!')
