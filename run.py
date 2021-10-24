import nltk
import os

nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

from pattern.en import pluralize, conjugate, PAST

import random

from colorama import Fore, Back, Style

from simple_term_menu import TerminalMenu


def main_madlib():
    """
    Asks for user input,
    checks the input,
    return the madlib formatted string 
    """
    noun1 = 'cat'
    verb1 = 'show'
    adj2 = 'furry'
    noun2 = 'robot'



    madlib = f'''
{Style.BRIGHT}{noun1} {verb1} and went to a {adj2} {noun2}.
'''
    print(madlib)


main_madlib()