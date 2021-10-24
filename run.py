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

    while not (len(adj1) >= 2 and adj1.isalpha()):
        adj1 = input('Type an adjective: ')
    while not (len(noun1) >= 2 and noun1.isalpha()):
        noun1 = input('Type a noun (living thing): ')
    while not (len(verb1) >= 2 and verb1.isalpha()):
        verb1 = input('Type a verb: ')
    while not (len(adj2) >= 2 and adj2.isalpha()):
        adj2 = input('Type an adjective: ')
    while not (len(noun2) >= 2 and noun2.isalpha()):
        noun2 = input('Type a noun: ')
    while not (len(famous_person) >= 2 and famous_person.isalpha()):
        famous_person = input("Type a famous person: ")
    while not (len(verb2) >= 2 and verb2.isalpha()):
        verb2 = input('Type a verb: ')
    while not (len(verb3) >= 2 and verb3.isalpha()):
        verb3 = input('Type a verb: ')
    while not (len(noun3) >= 2 and noun3.isalpha()):
        noun3 = input('Type a noun: ')
    while not (len(size_adjective1) >= 2 and size_adjective1.isalpha()):
        size_adjective1 = input('Type a size adjective: ')
    while not (len(color_adjective1) >= 2 and color_adjective1.isalpha()):
        color_adjective1 = input('Type a color adjective: ')
    while not (len(noun4) >= 2 and noun4.isalpha()):
        noun4 = input('Type a noun: ')
    while not (len(noun5) >= 2 and noun5.isalpha()):
        noun5 = input('Type a noun: ')
    while not (len(size_adjective2) >= 2 and size_adjective2.isalpha()):
        size_adjective2 = input('Type a size adjective: ')
    while not (len(color_adjective2) >= 2 and color_adjective2.isalpha()):
        color_adjective2 = input('Type a color adjective: ')
    while not (len(noun6) >= 2 and noun6.isalpha()):
        noun6 = input('Type a noun: ')
    while not (len(noun7) >= 2 and noun7.isalpha()):
        noun7 = input('Type a noun: ')
    while not (len(verb4) >= 2 and verb4.isalpha()):
        verb4 = input('Type a verb: ')


    madlib = f'''
{Style.BRIGHT}{noun1} {verb1} and went to a {adj2} {noun2}.
'''
    print(madlib)

main_madlib()