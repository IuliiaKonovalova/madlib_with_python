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
    elif (len(verb) > 2 and
        verb[-3] in dictionary_letters['consonant'] and
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

def choosing_article(*words):
    """
    Checks which article to use before the word and place the article before it
    """
    # Checks if the last word is countable.
    #If it is uncountable, returns all words
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

def choose_correct_form_be(word):
    if word in uncountable_nouns:
        return 'is'
    return 'are'

def run_the_time_error():
    """
    Prevent "RuntimeError: generator raised StopIteration"
    The package has raised StopIteration that was missed in python earier versions.
    Thus, it had worked before Python version 3.7 was introduced.
    Since the package has not been updates since August 2018, it raises the error and stops the app.
    "PEP 479 is enabled for all code in Python >= 3.7, meaning that StopIteration exceptions raised
    directly or indirectly in coroutines and generators are transformed
    into RuntimeError exceptions."
    Link to this change:
    https://docs.python.org/3/whatsnew/3.7.html#changes-in-python-behavior
    """
    try:
        conjugate(verb = '', tense = PAST)
    except RuntimeError:
        pass

run_the_time_error()

def draw_holes(mean):
    """
    Draws pictures of holes for the story
    """
    height = 7
    length = 21

    sth1 = '*' * length
    list1 = []
    for i in range(1, height, 2):
        sth2 = (i * (' ')).center(length, '*')
        list1.append(sth2)

    sth3 = "     ".upper().center(length, '*')

    list2 = []
    for j in range(height-2, -1, -2):
        sth4 = (j * (' ')).center(length, '*')
        list2.append(sth4)

    return f'{Fore.YELLOW}{sth1}\n    {list1[0]}\n    {list1[1]}\n    {list1[2]}\n    {sth3} {Fore.RED}{mean}\n    {Fore.YELLOW}{list2[0]}\n    {list2[1]}\n    {list2[2]}\n    {sth1}{Fore.RESET}'


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
    while len(adj1) < 2:
        adj1 = input('Type an adjective: ')
    while len(noun1) < 2:
        noun1 = input('Type a noun (living thing): ')
    while len(verb1) < 2:
        verb1 = input('Type a verb: ')
    while len(adj2) < 2:
        adj2 = input('Type an adjective: ')
    while len(noun2) < 2:
        noun2 = input('Type a noun: ')
    while len(famous_person) < 2:
        famous_person = input("Type a famous person: ")
    while len(verb2) < 2:
        verb2 = input('Type a verb: ')
    while len(verb3) < 2:
        verb3 = input('Type a verb: ')
    while len(noun3) < 2:
        noun3 = input('Type a noun: ')
    while len(size_adjective1) < 2:
        size_adjective1 = input('Type a size adjective: ')
    while len(color_adjective1) < 2:
        color_adjective1 = input('Type a color adjective: ')
    while len(noun4) < 2:
        noun4 = input('Type a noun: ')
    while len(noun5) < 2:
        noun5 = input('Type a noun: ')
    while len(size_adjective2) < 2:
        size_adjective2 = input('Type a size adjective: ')
    while len(color_adjective2) < 2:
        color_adjective2 = input('Type a color adjective: ')
    while len(noun6) < 2:
        noun6 = input('Type a noun: ')
    while len(noun7) < 2:
        noun7 = input('Type a noun (living thing): ')
    while len(verb4) < 2:
        verb4 = input('Type a verb: ')
    # Madlib formatted stringbig

    madlib = f'''
    {Style.BRIGHT}
    {choosing_article(adj1).capitalize()} {noun1} {conjugate(verb1, tense = PAST)} and went to {choosing_article(adj2, noun2)}.
    {formatting_pronoun(noun1).capitalize()} noticed {famous_person.title()} {verb_infinitive(verb2)}.
    {choosing_article(noun1).capitalize()} and {famous_person.title()} decided to {verb3} and have {choosing_article(size_adjective1, color_adjective1, noun3)} together.
    {Fore.BLUE}
    "It will cost an arm and a leg!"{Fore.WHITE} - said the {noun1}.
    {Fore.YELLOW}
    "Do not worry! I have a lot of {plural_noun(noun4)}! I can afford it!"
    {Fore.BLUE}
    "As you wish, {famous_person.title()}. You see, I am just a poor {noun1}... So I have only {plural_noun(noun5)}.
    If you want to share {choosing_a_quantifier(noun4)} {plural_noun(noun4)}, let's get it!"{Fore.WHITE} - said the {noun1}.

    And they started walking towards {choosing_article(size_adjective2, color_adjective2, noun6)}.
    It was already night when {famous_person.title()} noticed {choosing_article(size_adjective2, noun6)}.
    {Fore.BLUE}
    "Can you see it? We are here!"{Fore.WHITE} - said {famous_person.title()} while pointing at the {noun6}.
    {Fore.BLUE}
    "Oh, yes! But look at this old {noun7} in the bushes!"{Fore.WHITE} - says the {noun1}.

    The old {noun7} started walking slowly towards {famous_person.title()} and the {noun1}.
    Then, they saw that {formatting_pronoun(noun7)} was carrying a golden coin.
    As soon as {formatting_pronoun(noun7)} reached our travelers, {formatting_pronoun(noun7)} started {verb_infinitive(verb4)} and handed out that golden coin to them and left silently.
    {famous_person.title()} looked at the coin...
    There were several words colored in {color_adjective2} and a big {color_adjective2} rose drawn under them.

    {Fore.BLUE}"What is written there?"{Fore.WHITE} - asked the {noun1}.

    {Fore.YELLOW}"{idioms_list[0]}"{Fore.WHITE} - read out loud {famous_person.title()}.

    {Fore.YELLOW}"That's strange..."{Fore.WHITE} - {famous_person.title()} added.

    {Fore.BLUE}"Why the text and the rose on the coin are {color_adjective2}?"{Fore.WHITE} - pondered the {adj1} {noun1}.

    {Fore.YELLOW}"Maybe because the {size_adjective2} {noun6} is {color_adjective2}?"{Fore.WHITE} - {famous_person.title()} replied to {formatting_personal_pronoun(noun1)}.

    As soon as they got closer to the {size_adjective2} {color_adjective2} {noun6}, the {noun1} yelled:

    {Fore.BLUE}"That's it!"

    {Fore.WHITE}On the front side of the {size_adjective2} {color_adjective2} {noun6} were a picture of a small version of {choosing_article(size_adjective2, color_adjective2, noun6)} and a plate with 4 holes with sentences near them.
    {draw_holes(idioms_list[1][0])}
    {draw_holes(idioms_list[1][1])}
    {draw_holes(idioms_list[1][2])}
    {draw_holes(idioms_list[1][3])}

    {Fore.YELLOW}"As I've got it, we just need to {verb4} and throw our coin into the right hole."{Fore.WHITE} - said {famous_person.title()}.

    {Fore.BLUE}"Why do we need to {verb4} before throwing this coin?"{Fore.WHITE} - asked the {adj1} {noun1}.

    {Fore.YELLOW}"That's obvious! Because the old {noun7} was {verb_infinitive(verb4)}!"

    {Fore.BLUE}"Ok! Now you have to figure out which whole is needed."

    {Fore.YELLOW}"Why me? I am not so savvy!"

    {Fore.BLUE}"Look! I am just a poor {noun1}! I have only {plural_noun(noun5)}! No brain!
    So it is you, {famous_person.title()}, who have to make a decision!"

    {Fore.YELLOW}"Why me?"

    {Fore.BLUE}"It's deffinitely a strange question! The answer is simple -  because you have a lot of {plural_noun(noun4)} and you are famous!"

    {Fore.YELLOW}"That's fair... But still my {plural_noun(noun4)} {choose_correct_form_be(noun4)} not helpful here. Let me think...
    If I were an old {noun7}, what would I choose..."

    {Fore.WHITE}After pondering for an hour, {famous_person.title()} took a coin and through it into the hole with the sentence {Fore.RED}"{idioms_dictionary.get(idioms_list[0])}"{Fore.WHITE}.
    As soon as the coin disappeared in the hole, the ground opened up under them and swallowed them literally.
    They were falling down to nowhere... no light, no even a soul, just darkness everywhere...
    Eventually, the reached the ground.
    As luck would have it, they survived!

    {Fore.BLUE}"Why all of this is happenning to us?"{Fore.WHITE} - yelled the already terrified {noun1}.

    {Fore.YELLOW}"I sincerely can't get my head around this as well! It might be all about {choosing_article(size_adjective1, color_adjective1, noun3)}..."{Fore.WHITE} - replied {famous_person.title()}.

    {Fore.BLUE}"Yeah! I heard the the quality of the {size_adjective1} {color_adjective1} {noun3} is marvelous!"{Fore.WHITE}.

    Had it not been for the lack of light, they would have realized on time that they were not alone.
    Then the light turned on and they saw everything...
    They were in a huge room, where everything was colored in {color_adjective2}. They were surrounded by millions of old {plural_noun(noun7)} with their spears pointing at our travellers.

    {Fore.BLUE}"What's going on?"{Fore.WHITE} - whispered the poor {noun1}.

    {Fore.YELLOW}"Unacceptable! I am {famous_person.title()}! You have to know who I am! Let us go!"

    {Fore.RED}"Silence!"{Fore.WHITE} - one of the old {plural_noun(noun7)} ordered. - {Fore.RED}"You think you are allowed to be cocky!?"

    {Fore.YELLOW}"Ok, let's make a deal! You see, I am in possession of lots of {plural_noun(noun4)}! So I will give you half of my fortune if you let us go with {choosing_article(size_adjective1, color_adjective1, noun3)}"


    
    1. {idioms_list[1][0]}
    2. {idioms_list[1][1]}
    3. {idioms_list[1][2]}
    4. {idioms_list[1][3]}

    '''
    print(madlib)

def show_the_rules():
    """
    Shows the rules of the game
    """
    print(f'''
    {Fore.YELLOW}1. {Fore.WHITE}Follow the instructions!
    {Fore.YELLOW}2. {Fore.WHITE}Type the words correctly!
    {Fore.YELLOW}3. {Fore.WHITE}Don't cheat!
    ''')

def main():
    """
    Main program function
    """
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Shows welcoming message
    print(f'''
    {Fore.GREEN}Welcome to {Fore.YELLOW}Another Madlib Game!
    ''')
    main_madlib()

main()
