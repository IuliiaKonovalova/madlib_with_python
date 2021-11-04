import os
import random
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from time import sleep
import nltk
from pattern.en import pluralize, conjugate, PAST
from gender_words import dictionary_gender
from uncountable_nouns import uncountable_nouns
from idioms import idioms_dictionary

nltk.set_proxy('127.0.0.1:41091')
nltk.download('wordnet')

# Dictionary for vowels and consonants
dictionary_letters = {
    'vowels': [
        'a',
        'o',
        'i',
        'e',
        'u'
    ],
    'consonant': [
        'b',
        'c',
        'd',
        'f',
        'g',
        'h',
        'j',
        'k',
        'l',
        'm',
        'n',
        'p',
        'q',
        'r',
        's',
        't',
        'v',
        'w',
        'x',
        'y',
        'z'
    ]
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
    Since the package has not been updates since August 2018,
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
    size_adj1 = ''
    color_adj1 = ''
    noun4 = ''
    noun5 = ''
    size_adj2 = ''
    color_adj2 = ''
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
    while len(size_adj1) < 2:
        size_adj1 = input('Type a size adjective: ')
    while len(color_adj1) < 2:
        color_adj1 = input('Type a color adjective: ')
    while len(noun4) < 2:
        noun4 = input('Type a noun: ')
    while len(noun5) < 2:
        noun5 = input('Type a noun: ')
    while len(size_adj2) < 2:
        size_adj2 = input('Type a size adjective: ')
    while len(color_adj2) < 2:
        color_adj2 = input('Type a color adjective: ')
    while len(noun6) < 2:
        noun6 = input('Type a noun: ')
    while len(noun7) < 2:
        noun7 = input('Type a noun (living thing): ')
    while len(verb4) < 2:
        verb4 = input('Type a verb: ')
    # Madlib formatted string

    madlib_1 = f'''
{Style.BRIGHT}{Fore.WHITE}
{choose_article(adj1).capitalize()} {noun1}
{conjugate(verb1, tense = PAST)} and went to {choose_article(adj2, noun2)}.
{format_pronoun(noun1).title()} kept {verb_infinitive(verb1)} slowly
when noticed {choose_article(noun1)}
{famous_person.title()} {verb_infinitive(verb2)}.
{choose_article(noun1).capitalize()} and {famous_person.title()}
decided to {verb3} and have
{choose_article(size_adj1, color_adj1, noun3)} together.
    '''
    madlib_2 = f'''
{Fore.BLUE}"It will cost an arm and a leg!"{Fore.WHITE} - said the {noun1}.
{Fore.YELLOW}
"Do not worry! I have a lot of {plural_noun(noun4)}! I can afford it!"
{Fore.BLUE}
"As you wish, {famous_person.title()}. You see, I am just a poor {noun1}...
So I have only {plural_noun(noun5)}.
If you want to share {choosing_a_quantifier(noun4)} {plural_noun(noun4)},
let's get it!"{Fore.WHITE} - said the {noun1}.
    '''
    madlib_3 = f'''
And they started walking towards
{choose_article(size_adj2, color_adj2, noun6)}.
It was already night when {famous_person.title()} noticed
{choose_article(size_adj2, noun6)} on the horizon.
{Fore.BLUE}
"Can you see it? We are here!"{Fore.WHITE}
- said {famous_person.title()} while pointing at the {noun6}.
{Fore.BLUE}
"Oh, yes! But look at this old {noun7} in the bushes!"
{Fore.WHITE} - says the {noun1}.
    '''
    madlib_4 = f'''
The old {noun7} started walking slowly
towards {famous_person.title()} and the {noun1}.
Then, they saw that {format_pronoun(noun7)} was carrying a golden coin.
As soon as {format_pronoun(noun7)} reached our travelers,
{format_pronoun(noun7)} started {verb_infinitive(verb4)}
After {verb_infinitive(verb4)}, {noun7} handed out a golden
coin to them and left silently.
{famous_person.title()} looked at the coin...
There were several words colored in {color_adj2} and
a big {color_adj2} rose drawn under them.
    '''
    madlib_5 = f'''
{Fore.BLUE}"What is written there?"{Fore.WHITE} - asked the {noun1}.
{Fore.YELLOW}
"{idioms_list[0]}"{Fore.WHITE} - read out loud {famous_person.title()}.
{Fore.YELLOW}
"That's strange..."{Fore.WHITE} - {famous_person.title()} added.
{Fore.BLUE}
"Why the text and the rose on the coin are {color_adj2}?"
{Fore.WHITE}- pondered the {adj1} {noun1}.
{Fore.YELLOW}
"Maybe because the {size_adj2} {noun6} is {color_adj2}?"
{Fore.WHITE}
- {famous_person.title()} replied to {formatting_personal_pronoun(noun1)}.
    '''
    madlib_6 = f'''
As soon as they got closer to the {size_adj2} {color_adj2} {noun6},
the {noun1} yelled and started {verb_infinitive(verb1)}:
{Fore.BLUE}
"That's it!"
{Fore.WHITE}
On the front side of the {size_adj2} {color_adj2} {noun6} were
a picture of a small version of {choose_article(size_adj2, color_adj2, noun6)}
and a plate with 4 holes with sentences near them.
    '''
    madlib_7 = f'''
{draw_holes(idioms_list[1][0])}
    '''
    madlib_8 = f'''
{draw_holes(idioms_list[1][1])}
    '''
    madlib_9 = f'''
{draw_holes(idioms_list[1][2])}
    '''
    madlib_10 = f'''
{draw_holes(idioms_list[1][3])}
    '''
    madlib_11 = f'''
{Fore.YELLOW}"Listen, {noun1}! As I've got it,
we just need to {verb4} and throw our coin into the right hole."
{Fore.WHITE}- said {famous_person.title()}.
    '''
    madlib_12 = f'''
{Fore.BLUE}"Why do we need to {verb4} before throwing this coin?"
{Fore.WHITE}- asked the {adj1} {noun1}.
{Fore.YELLOW}
"That's obvious!
Because the old {noun7} was {verb_infinitive(verb4)}!"
{Fore.BLUE}
"Ok! Now you have to figure out which whole is needed."
{Fore.YELLOW}
"Why me? I am not so savvy!"
    '''
    madlib_13 = f'''
{Fore.BLUE}"Look! I am just a poor {noun1}!
I have only {plural_noun(noun5)}! No brain!
So it is you, {famous_person.title()}, who has to make a decision!"
{Fore.YELLOW}
"Why me?"
{Fore.BLUE}
"It's deffinitely a strange question!
The answer is simple: because you have a lot of {plural_noun(noun4)}
and you are famous!"
    '''
    madlib_14 = f'''
{Fore.YELLOW}"That's fair... But still my
{plural_noun(noun4)} {choose_correct_form_be(noun4)} not helpful here.
Let me think...
If I were an old {noun7}, what would I choose..."
{Fore.WHITE}
After pondering for an hour,
{famous_person.title()} took a coin and threw it
into the hole with the sentence:
{Fore.RED}
"{idioms_dictionary.get(idioms_list[0])}"{Fore.WHITE}.
        '''
    madlib_15 = f'''
As soon as the coin disappeared in the hole, the wind blew and
the ground opened up under them and swallowed them literally.
They were falling down to nowhere...
no light, no even a soul, just darkness everywhere...
Only {color_adj2} sky above them.
Eventually, the reached the ground.
As luck would have it, they survived!
    '''
    madlib_16 = f'''
{Fore.BLUE}"Why all of this is happenning to us?"
{Fore.WHITE} - yelled the already terrified {noun1}.
{Fore.YELLOW}
"I sincerely can't get my head around this as well!
It might be all about...
{choose_article(size_adj1, color_adj1, noun3)}..."
{Fore.WHITE}- replied {famous_person.title()}.
{Fore.BLUE}
"Yeah! I heard the the quality of
the {size_adj1} {color_adj1} {noun3}
is just marvelous!"
    '''
    madlib_17 = f'''
{Fore.WHITE}Had it not been for the lack of light,
they would have realized on time that they were not alone.
When the light turned on, they saw everything...
They were in a huge room, where everything was colored in {color_adj2}.
They were surrounded by millions of old {plural_noun(noun7)}
with their spears pointing at our travellers.
    '''
    madlib_18 = f'''
{Fore.BLUE}"What's going on?"
{Fore.WHITE} - whispered the poor {noun1}.
{Fore.YELLOW}
"Unacceptable! I am {famous_person.title()}!
You have to know who I am! Let us go!"
{Fore.RED}
"Silence!"{Fore.WHITE} - one of the old {plural_noun(noun7)} ordered.
{Fore.RED}"You think you are allowed to be cocky!?"
    '''
    madlib_19 = f'''
{Fore.YELLOW}"Ok, let's make a deal!
You see, I am in possession of lots of {plural_noun(noun4)}!
So I will give you half of my fortune if you simply let us go
with {choose_article(size_adj1, color_adj1, noun3)}"
{Fore.RED}
"Pathetic!"{Fore.WHITE} - the same old {noun7} responded -
{Fore.RED}Your {plural_noun(noun4)} {choose_correct_form_be(noun4)} nothing!
But you two stole the golden coin!"
    '''
    madlib_20 = f'''
{Fore.BLUE}"Excuse me, sir"{Fore.WHITE} - mumbled {noun1} -
{Fore.BLUE}"That's not true!
One of your {plural_noun(noun7)} gave it to us,
{conjugate(verb4, tense = PAST)}, and left silently".
{Fore.RED}
"Listen! You don't have the right to take anything from our folks!
But you did! Moreover, you also performed our thing!"
{Fore.BLUE}
"What thing? We did nothing! We just wanted to have
{choose_article(size_adj1, color_adj1, noun3)} together!"
    '''
    madlib_21 = f'''
{Fore.RED}"You {conjugate(verb4, tense = PAST)} on purpose!"
{Fore.WHITE}- the old {noun7} turned to
the old {plural_noun(noun7)} who were holding spears.
{Fore.RED}"Put them in prison! Now!".
{Fore.WHITE}
The {plural_noun(noun7)} with spears stepped forward and grabbed our travelers.
They were dragging them through endless {color_adj2} tunnel.
    '''
    madlib_22 = f'''
After some time they were kicked into a dark {color_adj2} prison cell.
{noun1.capitalize()} and {famous_person.title()} kept silence for a while.
{Fore.YELLOW}
"What's in your mind, {noun1}?"
{Fore.BLUE}
"What's in my mind? I'll tell you what's in my mind!
What's wrong with you, {famous_person.title()}?
You think that if you're famous and have a lot of {plural_noun(noun4)},
you are allowed to say what ever you want?"
    '''
    madlib_23 = f'''
{Fore.WHITE}Then they heard some wishper...
{Fore.MAGENTA}"Hello there!" - {Fore.WHITE}said unfamiliar voice.
Actually it was the {choose_article(adj2, noun2)}!
But they will never guess about this {noun2}
and what is awaiting them in the future.
{Fore.MAGENTA}
"Guys, I have something that might help you.
But you have to do one thing in return...
I'm pretty sure that you've got here because you just wanted
to get {choose_article(size_adj1, color_adj1, noun3)}.
Am I right?"
    '''
    madlib_24 = f'''
{Fore.BLUE}"Yes, you are right! Unfortunately, {famous_person.title()}
decided to break all rules and we've got here!
Do you know how to get out? If you do,
{famous_person.title()} will give you all of {plural_noun(noun4)}!"
{Fore.YELLOW}
"What are you talking about?
All of the {plural_noun(noun4)} {choose_correct_form_be(noun4)} mine!
Only I can make a call about what to do with {plural_noun(noun4)}!"
{Fore.BLUE}
"Shut up!
We're in the {color_adj2} prison of the {size_adj2} {color_adj2} {noun6}.
In addition, there is an army of old {plural_noun(noun7)} around us!
You are famous! You still can {verb2} and earn your {plural_noun(noun4)} back!
I do remember you {conjugate(verb2, tense = PAST)} when I met you!
Just do what this voice will say!"
    '''
    madlib_25 = f'''
{Fore.WHITE}{famous_person.title()} nodded in agreement.
{Fore.YELLOW}
"Ok. We will do what ever it takes to get out of this prison and
from this {size_adj2} {color_adj2} {noun6}!
Tell us what you want in return!"
{Fore.MAGENTA}
"You see I have some obligations.
I have other {adj2} {plural_noun(noun2)}.
I have to provide for {format_pronoun(noun2)}".
I will give you a little mirror and tell how to use it.
It will help you to escape from the old {plural_noun(noun7)}.
But you have to give everything that you have
to my {plural_noun(noun2)}.
{famous_person.title()}, you will give away all your {plural_noun(noun4)}.
And you, {adj1} {noun1}, will give away all of your {plural_noun(noun5)}.
Deal?"
    '''
    madlib_26 = f'''
{Fore.YELLOW} "How should we deliver all of the {plural_noun(noun4)}
and {plural_noun(noun5)} to your {plural_noun(noun2)}?"
{Fore.MAGENTA}
"You are quite practical, {famous_person.title()}, aren't you?
Do not worry about it.
As soon as you start following my instruction
your wealth will be with my {plural_noun(noun2)}."
{Fore.BLUE}
"Is it some kind of a magic?"
{Fore.MAGENTA}
"It depends on the perspective. Never mind.
Let's cut to the chase:
{noun1}, life and freedom or you keep your {plural_noun(noun5)}?
{famous_person.title()}, life and freedom or
you keep your {plural_noun(noun4)}?"
{Fore.BLUE}
"Life and freedom!"
{Fore.YELLOW}
"Life and freedom!"
    '''
    madlib_27 = f'''
{Fore.MAGENTA}"Excellent!
{famous_person.title()}, look the mirror and say:
I, {famous_person.title()}, give all my {plural_noun(noun4)} away willingly.
Then you have to make 5 jumps,
but after each jump you need to {verb4} every time.
You should do exactly what I said!
It's a secret ritual of the oldest {plural_noun(noun7)} and will give you
{adj2} power which helps you on your way back home!
{noun1}, you have to do the same, but speech will be different:
I, {noun1}, give all my {plural_noun(noun5)} away willingly and give you
my word not to hang out with {famous_person.title()}."
    '''
    madlib_28 = f'''
{Fore.BLUE}"I am not going to hang out with this person anyway!
Let's do it!"
{Fore.WHITE}
And our travelers did everything according to
the {choose_article(adj2, noun2)}'s instractions.
When they finished, {noun2} took the mirror back
and hand out 1 wooden box to the {noun1}
and 1 wooden box to {famous_person.title()}.
{Fore.MAGENTA}
"Each of you, place the box on your right hand
and put the lift hand above the box."
"Now shake it as hard as you can to let the key fall from the boxes."
{Fore.WHITE}
{famous_person.title()} and {noun1} did as the voice had ordered.
Eventually, they got the keys!
{Fore.MAGENTA}
"Hurry up! You have not much time!"
    '''
    madlib_29 = f'''
{Fore.WHITE}When our travelers left the tunnel, the {adj2} {noun2}
easily entered the cell where {famous_person.title()} and {noun1}
had stayed for a while. {format_pronoun(noun2).capitalize()} took
a camera out of the mirror and placed two boxes in
the bags for evidence.
As it turned out the {noun2} was actually not a {noun2} at all.
{format_pronoun(noun2).capitalize()} was a young attorney who'd lured
{noun1} and {famous_person.title()} into
having {choose_article(size_adj1, color_adj1, noun3)} together,
going to the {size_adj2} {color_adj2} {noun6},
taking the coin from the old {noun7},
throwing it to the right hole,
arguing with the army of old {plural_noun(noun7)},
getting in the prison,
and giving out all the {plural_noun(noun5)} and {plural_noun(noun4)} away.
    '''
    print(f'''
{Fore.GREEN}Be ready to read an amazing story...
    ''')
    sleep(2)
    print(madlib_1)
    sleep(7)
    print(madlib_2)
    sleep(10)
    print(madlib_3)
    sleep(10)
    print(madlib_4)
    sleep(10)
    print(madlib_5)
    sleep(10)
    print(madlib_6)
    sleep(8)
    print(madlib_7)
    sleep(2)
    print(madlib_8)
    sleep(2)
    print(madlib_9)
    sleep(2)
    print(madlib_10)
    sleep(2)
    print(madlib_11)
    sleep(3)
    print(madlib_12)
    sleep(8)
    print(madlib_13)
    sleep(8)
    print(madlib_14)
    sleep(8)
    print(madlib_15)
    sleep(20)
    print(madlib_16)
    sleep(15)
    print(madlib_17)
    sleep(15)
    print(madlib_18)
    sleep(8)
    print(madlib_19)
    sleep(10)
    print(madlib_20)
    sleep(15)
    print(madlib_21)
    sleep(10)
    print(madlib_22)
    sleep(12)
    print(madlib_23)
    sleep(15)
    print(madlib_24)
    sleep(20)
    print(madlib_25)
    sleep(15)
    print(madlib_26)
    sleep(15)
    print(madlib_27)
    sleep(15)
    print(madlib_28)
    sleep(15)
    print(madlib_29)
    sleep(20)


def show_the_rules():
    """
    Shows the rules of the game
    """
    print(f'''
    {Fore.YELLOW}1. {Fore.WHITE}Follow the instructions!
    {Fore.YELLOW}2. {Fore.WHITE}Type the words correctly!
    {Fore.YELLOW}3. {Fore.WHITE}Don't cheat!
    ''')
    sleep(1)


def main():
    """
    Main program function
    """
    # Clears the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    # Shows welcoming message
    print(f'''
{Fore.GREEN}Welcome to {Fore.YELLOW}The Maddest Madlib!
    ''')
    user_name = ''
    # Ask user's name
    while len(user_name) < 2:
        user_name = input('Please enter your name: ').title()
    print(f'''
{Fore.GREEN}
Greeting to you, {Fore.YELLOW}{user_name}{Fore.GREEN}!
I hope you are doing well!
Please, pick an option in the {Fore.YELLOW}menu!
    ''')
    sleep(1)
    options = ['1. Learn the rules', '2. Start the game', '3. Quit']
    main_menu = TerminalMenu(options)
    quitting = False
    while quitting is not True:
        options_index = main_menu.show()
        options_choice = options[options_index]
        if options_choice == '3. Quit':
            print(f'''
{Fore.GREEN}
I hope you had some fun, {Fore.YELLOW}{user_name}{Fore.GREEN}!
Thanks for using this app!
See you soon here, {Fore.YELLOW}{user_name}{Fore.GREEN}!
{Style.BRIGHT}
{Fore.RED}P.S.
{Fore.GREEN}The author of the program was sober
at all stages of creating this story.
            ''')
            quitting = True
        elif options_choice == '1. Learn the rules':
            print(f'''
{Fore.YELLOW}{user_name}{Fore.GREEN},
Please read the rules attentively and follow them precisely!
            ''')
            sleep(1)
            show_the_rules()
        else:
            print(f'''
{Fore.GREEN}Be ready to type words...
            ''')
            sleep(2)
            main_madlib()
            print(f'''
{Fore.GREEN}The end.{Fore.WHITE}{Style.RESET_ALL}
            ''')

main()
