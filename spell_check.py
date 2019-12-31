import os
import pandas as pd
from textblob import Word
from data_utils import file
from tools import display


class spell(object):
    def __init__(self):
        self.PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
        os.chdir(self.PATH)
        self.col = ["word", "etymonline", "emeaning", "cmeaning"]
        self.default_name = 'C.csv'  # default file to be open

    def spell_check(self, word_input):
        correct = True
        w = Word(word_input)
        # ans = w.spellcheck()
        ans = w.correct()
        if ans != w:
            correct = False
        return ans, correct

    def spell_check_all(self):
        incorrect_list = pd.DataFrame(
            columns=['word', 'emeaning_old', 'emeaning_new'])
        source = file().load_data('B.csv')
        check = source["emeaning"]
        check = check.dropna()
        # print(check.describe())
        count = 0
        for row in check:
            print('current: ', row)
            ans, correct = self.spell_check(row)
            if correct == False:
                print(row, ans)
                print(display(source.loc[source.emeaning == row].word))
                incorrect_list = incorrect_list.append(
                    {"word": source.loc[source.emeaning == row].word.item(), "emeaning_old": row, "emeaning_new": ans}, ignore_index=True)
                count += 1
            if count % 10 == 0:
                file().save_csv(incorrect_list, 'B_.csv')

        file().save_csv(incorrect_list, 'B_.csv')


print(spell().spell_check_all())
