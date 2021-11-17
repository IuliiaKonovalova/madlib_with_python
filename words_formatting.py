import random
import nltk
from colorama import Fore
from pattern.en import pluralize, conjugate, PAST
from gender_words import dictionary_gender
from uncountable_nouns import uncountable_nouns
from idioms import idioms_dictionary
from dictionary_letters import dictionary_letters

nltk.download('wordnet')


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
            (verb[-1] == 'c' and verb[-1] == 'h')):
        # if 1 of the conditions are true, adds 'es'
        formatted_verb = verb + 'es'
    # Adds 's' to the end of the input word in other cases
    else:
        formatted_verb = verb + 's'
    return formatted_verb


def format_pronoun(noun):
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


def formatting_reflexive_pronoun(noun):
    """
    Checks the noun whether it is a female or male noun,
    places the correct personal pronoun when it is needed
    """
    # Checks if the word classified as female, replace the word with 'her'
    if noun in dictionary_gender['female']:
        pronoun = 'herself'
    # Checks if the word classified as male, replace the word with 'him'
    elif noun in dictionary_gender['male']:
        pronoun = 'himself'
    # Otherwise, returns 'it'
    else:
        pronoun = 'itself'
    return pronoun


def verb_infinitive(verb):
    """
    Format verb into infinitive
    """
    # Check if the verb ends with 'ie', changes 'ie' into 'ying'
    if verb[-2] == 'i' and verb[-1] == 'e':
        infinitive_verb = verb[:-2] + 'ying'

    # Check if the verb ends with 'e', changes 'e' to 'ing'
    elif verb[-1] == 'e':
        infinitive_verb = verb[:-1] + 'ing'

    # Checks if the verb ends vowel and consonant
    # Adds 1 more consonant and 'ing'
    elif (len(verb) > 2 and
            verb[-3] in dictionary_letters['consonant'] and
            verb[-2] in dictionary_letters['vowels'] and
            verb[-1] in dictionary_letters['consonant'] and
            verb[-1] != 'w'):
        # Since all three conditions are true, add 1 more consonant and 'ing'
        infinitive_verb = verb + verb[-1] + 'ing'

    #  Otherwise adds 'ing' to the verb
    else:
        infinitive_verb = verb + 'ing'

    return infinitive_verb


def plural_noun(noun):
    """
    Checks whether the noun is countable or not,
    transform into plural if it's countable
    This function is needed to prevent
    pluralization of uncountable nouns bt pattern package
    """
    # Checks if the noun is uncountable, if it is, returns the nouns
    if noun in uncountable_nouns:
        return noun
    # Otherwise, pluralize noun with the patterns package
    return pluralize(noun)


def choose_article(*words):
    """
    Checks which article to use before the word and place the article before it
    """
    # Checks if the last word is countable.
    # If it is uncountable, returns all words
    if words[-1] in uncountable_nouns:
        return ' '.join(words)
    else:
        # Checks if the word starts with a vowel, adds 'an' before the word
        if words[0][0] in dictionary_letters['vowels']:
            return 'an ' + ' '.join(words)
        # Otherwise, adds 'a' before the word
        else:
            return 'a ' + ' '.join(words)


def choosing_a_quantifier(noun):
    """
    Checks whether the noun is countable or not,
    transform into plural if it's countable
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
    while len(meanings) != 4:
        mean = random.choice(shuffle_meanings)
        # Check whether the meaning haven't been used already
        if mean not in meanings:
            meanings.append(mean)
    random.shuffle(meanings)
    # Create nested list with idiom and its meaning, plus 3 random meanings
    main_list = [shuffle_idioms[0], meanings]
    return main_list

idioms_list = random_idiom()


def choose_correct_form_be(word):
    if word in uncountable_nouns:
        return 'is'
    return 'are'


def run_the_time_error():
    """
    Prevent "RuntimeError: generator raised StopIteration"
    The package has raised StopIteration,
    that was missed in python earier versions.
    Thus, it had worked before Python version 3.7 was introduced.
    Since the package has not been updated since August 2018,
    it raises the error and stops the app.
    "PEP 479 is enabled for all code in Python >= 3.7,
    meaning that StopIteration exceptions raised
    directly or indirectly in coroutines and generators are transformed
    into RuntimeError exceptions."
    Link to this change:
    https://docs.python.org/3/whatsnew/3.7.html#changes-in-python-behavior
    """
    try:
        conjugate(verb='', tense=PAST)
    except RuntimeError:
        pass

run_the_time_error()


def draw_holes(mean):
    """
    Draws pictures of holes for the story
    """
    height = 7
    length = 21
    # Drawing the upper part of the image
    sth1 = '*' * length
    list1 = []
    for i in range(1, height, 2):
        sth2 = (i * (' ')).center(length, '*')
        list1.append(sth2)
    # Drawing the center part of the image
    sth3 = "     ".upper().center(length, '*')
    # Drawing the lower part of the image
    list2 = []
    for j in range(height-2, -1, -2):
        sth4 = (j * (' ')).center(length, '*')
        list2.append(sth4)
    return f'''{Fore.YELLOW}{sth1}
{sth1}
{list1[0]}
{list1[1]}
{list1[2]}
{sth3} {Fore.RED}{mean}
{Fore.YELLOW}{list2[0]}
{list2[1]}
{list2[2]}
{sth1}
{sth1}{Fore.RESET}'''
