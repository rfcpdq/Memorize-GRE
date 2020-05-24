from bs4 import BeautifulSoup
import urllib.request
from termcolor import cprint


def online_ety_single(word):
    etyURL = 'https://www.etymonline.com/search?q='
    AGENT = {'User-Agent': "Magic Browser"}
    
    url = etyURL + word
    req = urllib.request.Request(url, headers=AGENT)
    response = urllib.request.urlopen(req)
    html = response.read()
    
    page = BeautifulSoup(html, 'html.parser')
    # print(page.find("a", class_="word__name--TTbAA word_thumbnail__name--1khEg").get_text())
    
    if page.find("section", class_="word__defination--2q7ZH undefined"):
        rev_print = '|| ' + word + ' ||'
        cprint('=' * len(rev_print), 'green', attrs=['bold'])
        cprint(rev_print, 'green', attrs=['bold'])
        cprint('=' * len(rev_print), 'green', attrs=['bold'])
        # print(page.find("section", class_="word__defination--2q7ZH undefined").get_text().replace('\n', '\n\n'))
        print(page.find("section", class_="word__defination--2q7ZH undefined").get_text())

    else:
        cprint('Not Find!', 'green', attrs=['bold'])


def online_ety(word):
    etyURL = 'https://www.etymonline.com/search?q='
    AGENT = {'User-Agent': "Magic Browser"}
    
    url = etyURL + word
    req = urllib.request.Request(url, headers=AGENT)
    response = urllib.request.urlopen(req)
    html = response.read()

    page = BeautifulSoup(html, 'html.parser')
    
    if page.find("section", class_="word__defination--2q7ZH undefined"):
        nameList = page.find_all("a", class_="word__name--TTbAA word_thumbnail__name--1khEg")
        etyList = page.find_all("section", class_="word__defination--2q7ZH undefined")
        # print(len(nameList), len(etyList))
    
        for i in range(len(nameList)):
            rev_print = '|| ' + nameList[i].text + ' ||'
            cprint('=' * len(rev_print), 'green', attrs=['bold'])
            cprint(rev_print, 'green', attrs=['bold'])
            cprint('=' * len(rev_print), 'green', attrs=['bold'])
            print(etyList[i].text)
            print()
    
    else:
        cprint('Not Find!', 'green', attrs=['bold'])
