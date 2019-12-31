import time
import subprocess
from os import system, name


def clear():
    # another way to achieve this is: subprocess.call
    if name == 'nt':
        _ = system('cls')
    else:  # for mac and linux(here, os.name is 'posix')
        _ = system('clear')


def display(lista):
    lista = lista.astype(str)
    lista = [el.replace('\xa0', ' ') for el in lista]
    lista = [el.replace('\n', ' ') for el in lista]
    return lista


def adb_func(move):
    # Android pointer location
    # switch words
    if move == 'n':
        cmdCommand = "adb shell input swipe 700 700 300 700"
    if move == 'b':
        cmdCommand = "adb shell input swipe 700 700 1100 700"
    # next unit
    if move == 'next':
        cmdCommand = "adb shell input tap 270 2155"
        # cmdCommand = "adb shell input tap 270 2230"
    if move == 'next2':
        cmdCommand = "adb shell input tap 530 1355"
        # cmdCommand = "adb shell input tap 530 1430"
        time.sleep(1)
        cmdCommand = "adb shell input tap 270 2155"
        # cmdCommand = "adb shell input tap 270 2230"
    # review
    if move == '1':
        cmdCommand = "adb shell input tap 760 1990"
    if move == '2':
        cmdCommand = "adb shell input tap 310 1990"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
