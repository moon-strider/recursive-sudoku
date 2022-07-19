import utils.board
from utils.cli import cli
from utils.misc import glob
from utils.misc import misc
from utils.misc import loc


import pandas as pd


def setLanguage() -> str:
    lang = ""
    while not lang:
        print("Please select a valid language: ")
        for i in glob.lang_list:
            print(i)
        lang = misc.getCommand(
            msg := "Select your language: ", 
            lang := input(msg), 
            glob.lang_list
            )


if __name__ == "__main__":
    lang = setLanguage()
    misc.clear()
    print(loc.welcome[lang])