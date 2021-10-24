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
    adj1 = ''
    noun1 = ''
    verb1 = ''
    adj2 = ''
    noun2 = ''
    famous_person = ''
    verb2 = ''
    verb3 = ''
    noun3 = ''
    size_adjective1 = ''
    color_adjective1 = ''
    noun4 = ''
    noun5 = ''
    size_adjective2 = ''
    color_adjective2 = ''
    noun6 = ''
    noun7 = ''
    verb4 = ''


    madlib = f'''
{Style.BRIGHT}{noun1} {verb1} and went to a {adj2} {noun2}.
'''
    print(madlib)

main_madlib()