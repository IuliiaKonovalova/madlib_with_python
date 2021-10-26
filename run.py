import os
import random
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
import nltk
from pattern.en import pluralize, conjugate, PAST
from gender_words import dictionary_gender
from uncountable_nouns import uncountable_nouns
from idioms import idioms_dictionary

nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

# Dictionary for vowels and consonants
dictionary_letters = {
    'vowels': ['a', 'o', 'i', 'e', 'u'],
    'consonant': ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
}


def verb_formatting(verb):
    """
    Checks the verb and changes the form of a verb for a sentense
    """
    # Checks if the word ends with 'y', changes 'y' into 'ies'
    if verb[-1] == 'y':
        formatted_verb = verb[:-1] + 'ies'
    # Checks if the input verb is 'have', changes 'has'
    elif verb == 'have':
        formatted_verb = verb[:-2] + 's'
    # Checks if the word ends with 'o, s, z, x, ch, changes ending into 'es'
    elif (verb[-1] == 'o' or
          verb[-1] == 's' or
          verb[-1] == 'z' or
          verb[-1] == 'x' or
          (verb[-1] == 'c' and verb[-1] =='h')):
          # Since 1 of the conditions are true, add 'es'
        formatted_verb = verb + 'es'
    # Adds 's' to the end of the input word in other cases
    else:
        formatted_verb = verb + 's'
    return formatted_verb

def formatting_pronoun(noun):
    """
    Checks the noun whether it is a female or male noun
    """
    # Checks whether the word is female, returns 'she'
    if noun in dictionary_gender['female']:
        pronoun = 'she'
    # Checks whether the word is male, returns 'he'
    elif noun in dictionary_gender['male']:
        pronoun = 'he'
    # If the word gender neutral, returns 'it'
    else:
        pronoun = 'it'
    return pronoun

def formatting_personal_pronoun(noun):
    """
    Checks the noun whether it is a female or male noun,
    places the correct personal pronoun when it is needed
    """
    # Checks if the word classified as female, replace the word with 'her'
    if noun in dictionary_gender['female']:
        pronoun = 'her'
    # Checks if the word classified as male, replace the word with 'him'
    elif noun in dictionary_gender['male']:
        pronoun = 'him'
    # Otherwise, returns 'it'
    else:
        pronoun = 'it'
    return pronoun

def verb_infinitive(verb):
    """
    Format verb into infinitive
    """
    # Check if the verb ends with 'ie', changes 'ie' into 'ying'
    if verb[-2] == 'i' and verb[-1] == 'e':
        infinitive_verb = verb[:-2] + 'ying'
    # Check if the verb ends with 'e', changes 'e' into 'ing'
    elif  verb[-1] == 'e':
        infinitive_verb = verb[:-1] + 'ing'
    #  Checks if the verb ends vowel and consonant, adds 1 more consonant and 'ing'
    elif (verb[-3] in dictionary_letters['consonant'] and
        verb[-2] in dictionary_letters['vowels'] and
        verb[-1] in dictionary_letters['consonant']):
        # Since all three conditions are true, add 1 more consonant and 'ing'
        infinitive_verb  = verb + verb[-1] + 'ing'
    #  Otherwise adds 'ing' to the verb
    else:
        infinitive_verb = verb + 'ing'

    return infinitive_verb

def plural_noun(noun):
    """
    Checks whether the noun is countable or not and transform into plural if it's countable
    This function is needed to prevent pluralization of uncountable nouns bt pattern package
    """
    # Checks if the noun is uncountable, if it is, returns the nouns
    if noun in uncountable_nouns:
        return noun
    # Otherwise, pluralize noun with the patterns package
    return pluralize(noun)

def choosing_article(word):
    """
    Checks which article to use before the word and place the article before it
    """
    # Checks if the word starts with a vowel, adds 'an' before the word
    if word[0] in dictionary_letters['vowels']:
        return f'an {word}'
    # Otherwise, adds 'a' before the word
    return f'a {word}'

def choosing_a_quantifier(noun):
    """
    Checks whether the noun is countable or not and transform into plural if it's countable
    """
    # Checks if the word is uncountable, if yes, adds 'some' before the word
    if noun in uncountable_nouns:
        return 'some'
    # Otherwise, returns several before the word
    return 'several'

def random_idiom():
    """
    Takes random idiom from the dictionary,
    Takes its meaning
    Takes 3 more meanings of random idioms from the dictionary
    Returns nested list
    """
    # Get a random idiom from the keys in idioms dictionary
    shuffle_idioms = list(idioms_dictionary.keys())
    random.shuffle(shuffle_idioms)
    shuffle_meanings = list(idioms_dictionary.values())
    random.shuffle(shuffle_meanings)
    # Create list for idioms' meanings
    meanings = []
    # Push meaning of chosen idiom to this list
    main_meaning = idioms_dictionary[shuffle_idioms[0]]
    meanings.append(main_meaning)
    # Add 3 more random meanings to the list of meanings
    for mean in range(4):
        mean = random.choice(shuffle_meanings)
        meanings.append(mean)
    random.shuffle(meanings)
    # Create nested list with random idiom and its meaning, plus 3 random meanings
    main_list = [shuffle_idioms[0], meanings]
    return main_list

idioms_list = random_idiom()

def main_madlib():
    """
    Asks for user input, checks the input, return the madlib formatted string
    """
    # Variables for a user's input
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
    # Check the the user's inputs
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
    # Madlib formatted string
    madlib = f'''
{Style.BRIGHT}{noun1} {verb1} and went to a {adj2} {noun2}.
    '''
    print(madlib)

main_madlib()