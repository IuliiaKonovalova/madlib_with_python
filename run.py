import nltk
import os

nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

from pattern.en import pluralize, conjugate, PAST

import random

from colorama import Fore, Back, Style

from simple_term_menu import TerminalMenu


