from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from words_formatting import *


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
        adj1 = input('Type an adjective: ').strip()
    while len(noun1) < 2:
        noun1 = input('Type a noun (living thing): ').strip()
    while len(verb1) < 2:
        verb1 = input('Type a verb: ').strip()
    while len(adj2) < 2:
        adj2 = input('Type an adjective: ').strip()
    while len(noun2) < 2:
        noun2 = input('Type a noun: ').strip()
    while len(famous_person) < 2:
        famous_person = input("Type a famous person: ").strip()
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip()
    while len(verb3) < 2:
        verb3 = input('Type a verb: ').strip()
    while len(noun3) < 2:
        noun3 = input('Type a noun: ').strip()
    while len(size_adj1) < 2:
        size_adj1 = input('Type a size adjective: ').strip()
    while len(color_adj1) < 2:
        color_adj1 = input('Type a color adjective: ').strip()
    while len(noun4) < 2:
        noun4 = input('Type a noun: ').strip()
    while len(noun5) < 2:
        noun5 = input('Type a noun: ').strip()
    while len(size_adj2) < 2:
        size_adj2 = input('Type a size adjective: ').strip()
    while len(color_adj2) < 2:
        color_adj2 = input('Type a color adjective: ').strip()
    while len(noun6) < 2:
        noun6 = input('Type a noun: ').strip()
    while len(noun7) < 2:
        noun7 = input('Type a noun (living thing): ').strip()
    while len(verb4) < 2:
        verb4 = input('Type a verb: ').strip()
    # Madlib formatted string

    madlib_1 = [
        f'''
{Fore.YELLOW}Somewhere far far away...
    ''',
        f'''s
{Style.BRIGHT}{Fore.WHITE}
{choose_article(adj1).capitalize()} {noun1}
{conjugate(verb1, tense = PAST)} and went to {choose_article(adj2, noun2)}.
{format_pronoun(noun1).title()} kept {verb_infinitive(verb1)} slowly
when noticed
{famous_person.title()} {verb_infinitive(verb2)}.
{choose_article(noun1).capitalize()} and {famous_person.title()}
decided to {verb3} and have
{choose_article(size_adj1, color_adj1, noun3)} together.
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"It will cost an arm and a leg!"
{Fore.WHITE}- said the {noun1}.
{Fore.YELLOW}
"Do not worry! I have a lot of {plural_noun(noun4)}! I can afford it!"
{Fore.BLUE}
"As you wish, {famous_person.title()}. You see, I am just a poor {noun1}...
So I have only {plural_noun(noun5)}.
If you want to share {choosing_a_quantifier(noun4)} {plural_noun(noun4)},
let's get it!"{Fore.WHITE} - said the {noun1}.
    ''',
        f'''
{Style.BRIGHT}And they started walking towards
{choose_article(size_adj2, color_adj2, noun6)}.
It was already night when {famous_person.title()} noticed
{choose_article(size_adj2, noun6)} on the horizon.
{Fore.BLUE}
"Can you see it? We are here!"{Fore.WHITE}
- said {famous_person.title()} while pointing at the {noun6}.
{Fore.BLUE}
"Oh, yes! But look at this old {noun7} in the bushes!
{format_pronoun(noun7)} {verb_formatting(verb4)}"
{Fore.WHITE} - says the {noun1}.
    ''',
        f'''
{Style.BRIGHT}The old {noun7} started walking slowly
towards {famous_person.title()} and the {noun1}.
Then, they saw that {format_pronoun(noun7)} was carrying a golden coin.
As soon as {format_pronoun(noun7)} reached our travelers,
{format_pronoun(noun7)} started {verb_infinitive(verb4)}
After {verb_infinitive(verb4)}, {noun7} handed out a golden
coin to them and left silently.
{famous_person.title()} looked at the coin...
There were several words colored in {color_adj2} and
a big {color_adj2} rose drawn under them.
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"What is written there?"{Fore.WHITE}
- asked the {noun1}.
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
    ''',
        f'''
{Style.BRIGHT}As soon as they got closer to
the {size_adj2} {color_adj2} {noun6},
the {noun1} yelled and started {verb_infinitive(verb1)}:
{Fore.BLUE}
"That's it!"
{Fore.WHITE}
On the front side of the {size_adj2} {color_adj2} {noun6} were
a picture of a small version of {choose_article(size_adj2, color_adj2, noun6)}
and a plate with 4 holes with sentences near them.
    ''',
        f'''
{Style.BRIGHT}
{draw_holes(idioms_list[1][0])}
    ''',
        f'''
{Style.BRIGHT}
{draw_holes(idioms_list[1][1])}
    ''',
        f'''
{Style.BRIGHT}
{draw_holes(idioms_list[1][2])}
    ''',
        f'''
{Style.BRIGHT}
{draw_holes(idioms_list[1][3])}
    ''',
        f'''
{Style.BRIGHT}{Fore.YELLOW}"Listen, {noun1}! As I've got it,
we just need to {verb4} and throw our coin into the right hole."
{Fore.WHITE}- said {famous_person.title()}.
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"Why do we need to {verb4} before
throwing this coin?"{Fore.WHITE}- asked the {adj1} {noun1}.
{Fore.YELLOW}
"That's obvious!
Because the old {noun7} was {verb_infinitive(verb4)}!"
{Fore.BLUE}
"Ok! Now you have to figure out which whole is needed."
{Fore.YELLOW}
"Why me? I am not so savvy!"
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"Look! I am just a poor {noun1}!
I have only {plural_noun(noun5)}! No brain!
So it is you, {famous_person.title()}, who has to make a decision!"
{Fore.YELLOW}
"Why me?"
{Fore.BLUE}
"It's deffinitely a strange question!
The answer is simple: because you have a lot of {plural_noun(noun4)}
and you are famous!"
    ''',
        f'''
{Style.BRIGHT}{Fore.YELLOW}"That's fair... But still my
{plural_noun(noun4)} {choose_correct_form_be(noun4)} not helpful here.
Let me think...
If I were an old {noun7}, what would I choose..."
{Fore.WHITE}
After pondering for an hour,
{famous_person.title()} took a coin and threw it
into the hole with the sentence:
{Fore.RED}
"{idioms_dictionary.get(idioms_list[0])}"{Fore.WHITE}.
    ''',
        f'''
{Style.BRIGHT}As soon as the coin disappeared in the hole,
the wind blew and the ground opened up under them and swallowed them literally.
They were falling down to nowhere...
no light, no even a soul, just darkness everywhere...
Only {color_adj2} sky above them.
Eventually, the reached the ground.
As luck would have it, they survived!
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"Why all of this is happenning to us?"
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
    ''',
        f'''
{Style.BRIGHT}{Fore.WHITE}Had it not been for the lack of light,
they would have realized on time that they were not alone.
When the light turned on, they saw everything...
They were in a huge room, where everything was colored in {color_adj2}.
They were surrounded by millions of old {plural_noun(noun7)}
with their spears pointing at our travellers.
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"What's going on?"
{Fore.WHITE} - whispered the poor {noun1}.
{Fore.YELLOW}
"Unacceptable! I am {famous_person.title()}!
You have to know who I am! Let us go!"
{Fore.RED}
"Silence!"{Fore.WHITE} - one of the old {plural_noun(noun7)} ordered.
{Fore.RED}"You think you are allowed to be cocky!?"
    ''',
        f'''
{Style.BRIGHT}{Fore.YELLOW}"Ok, let's make a deal!
You see, I am in possession of lots of {plural_noun(noun4)}!
So I will give you half of my fortune if you simply let us go
with {choose_article(size_adj1, color_adj1, noun3)}"
{Fore.RED}
"Pathetic!"{Fore.WHITE} - the same old {noun7} responded -
{Fore.RED}Your {plural_noun(noun4)} {choose_correct_form_be(noun4)} nothing!
But you two stole the golden coin!"
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"Excuse me, sir"{Fore.WHITE} - mumbled {noun1} -
{Fore.BLUE}"That's not true!
One of your {plural_noun(noun7)} gave it to us,
{conjugate(verb4, tense = PAST)}, and left silently".
{Fore.RED}
"Listen! You don't have the right to take anything from our folks!
But you did! Moreover, you also performed our thing!"
{Fore.BLUE}
"What thing? We did nothing! We just wanted to have
{choose_article(size_adj1, color_adj1, noun3)} together!"
    ''',
        f'''
{Style.BRIGHT}{Fore.RED}"You {conjugate(verb4, tense = PAST)} on purpose!"
{Fore.WHITE}- the old {noun7} turned to
the old {plural_noun(noun7)} who were holding spears.
{Fore.RED}"Put them in prison! Now!".
{Fore.WHITE}
The {plural_noun(noun7)} with spears stepped forward and grabbed our travelers.
They were dragging them through endless {color_adj2} tunnel.
    ''',
        f'''
{Style.BRIGHT}After some time they were kicked into
a dark {color_adj2} prison cell.
{noun1.capitalize()} and {famous_person.title()} kept silence for a while.
{Fore.YELLOW}
"What's in your mind, {noun1}?"
{Fore.BLUE}
"What's in my mind? I'll tell you what's in my mind!
What's wrong with you, {famous_person.title()}?
You think that if you're famous and have a lot of {plural_noun(noun4)},
you are allowed to say what ever you want?"
    ''',
        f'''
{Style.BRIGHT}{Fore.WHITE}Then they heard some wishper...
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
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"Yes, you are right! Unfortunately,
{famous_person.title()} decided to break all rules and we've got here!
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
    ''',
        f'''
{Style.BRIGHT}{Fore.WHITE}{famous_person.title()} nodded in agreement.
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
    ''',
        f'''
{Style.BRIGHT}{Fore.YELLOW}"How should we deliver all of the
{plural_noun(noun4)} and {plural_noun(noun5)}
to your {plural_noun(noun2)}?"
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
    ''',
        f'''
{Style.BRIGHT}{Fore.MAGENTA}"Excellent!
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
    ''',
        f'''
{Style.BRIGHT}{Fore.BLUE}"I am not going to hang out with this person anyway!
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
    ''',
        f'''
{Style.BRIGHT}{Fore.WHITE}When our travelers left the tunnel, the {adj2}
{noun2} easily entered the cell where {famous_person.title()} and {noun1}
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
    ]
    for paragraph in madlib_1:
        if paragraph == madlib_1[-1]:
            print(paragraph)
            break
        print(paragraph)
        options = ['Continue']
        main_menu = TerminalMenu(options)
        main_menu.show()


def main_madlib_2():
    """
    Asks for user input, checks the input,
    prints the madlib strings with time interval
    """
    # Variables for a user's input
    adj1 = ''
    noun1 = ''
    verb1 = ''
    adj2 = ''
    noun2 = ''
    verb2 = ''
    noun3 = ''
    adj3 = ''
    noun4 = ''

    while len(adj1) < 2:
        adj1 = input('Type an adjective: ').strip()
    while len(noun1) < 2:
        noun1 = input('Type a noun (living thing): ').strip()
    while len(verb1) < 2:
        verb1 = input('Type a verb: ').strip()
    while len(adj2) < 2:
        adj2 = input('Type an adjective: ').strip()
    while len(noun2) < 2:
        noun2 = input('Type a noun: ').strip()
    while len(verb2) < 2:
        verb2 = input('Type a verb: ').strip()
    while len(noun3) < 2:
        noun3 = input('Type a noun: ').strip()
    while len(adj3) < 2:
        adj3 = input('Type a adjective: ').strip()
    while len(noun4) < 2:
        noun4 = input('Type a noun: ').strip()
    madlib_2 = f'''
{Style.BRIGHT}{Fore.WHITE}
A long time ago...
In a galaxy named {Fore.YELLOW}{noun2.capitalize()}{Fore.WHITE}...
{Fore.BLUE}{plural_noun(noun1).capitalize()}{Fore.WHITE} were living in peace.
These {Fore.BLUE}{plural_noun(noun1)}{Fore.WHITE} loved
{verb_infinitive(verb1)} very much.
They {conjugate(verb1, tense = PAST)} without stopping because
of their belief that {Fore.YELLOW}the {noun2.capitalize()} galaxy{Fore.WHITE}
was thriving on their favorite activity: {verb_infinitive(verb1)}.

There were thousands of planets in this galaxy and almost all of them were
inhabited with {Fore.BLUE}{plural_noun(noun1)}{Fore.WHITE}.
Some were {adj1} and some were {adj2}.

The main purpose of their lives was to earn
{Fore.YELLOW}the {noun2.capitalize()} status{Fore.WHITE}.
This status meant everything to the {Fore.BLUE}{plural_noun(noun1)}
{Fore.WHITE}, no matter whether they were {adj1} or {adj2}.
{Fore.BLUE}{choose_article(noun2).capitalize()}{Fore.WHITE}, which reached
{Fore.YELLOW}the {noun2.capitalize()} status{Fore.WHITE} were called
{Fore.YELLOW}{noun2.capitalize()}-master{Fore.WHITE}.

{Fore.YELLOW}{noun2.capitalize()}-masters{Fore.WHITE} were empowered to learn
about other galaxies and even explore them.
To obtain this status, {Fore.BLUE}{plural_noun(noun1)}{Fore.WHITE} had to
exchange goods with each other without any quarrels and {verb1} as much
as possible during their lives.

The most fascinating thing about all this {Fore.YELLOW}{noun2.capitalize()}
galaxy{Fore.WHITE} was that they were using {plural_noun(noun3)}
to communicate with each other inside their galaxy.
Of course, only {Fore.YELLOW}{noun2.capitalize()}-masters{Fore.WHITE}
were aware of how to built those {plural_noun(noun3)}.
This meant that common {Fore.BLUE}{plural_noun(noun1)}{Fore.WHITE} depended on
masters a lot. However, masters needed to get materials to built
{plural_noun(noun3)}. And those materials were in the Galaxy called
{Fore.RED}{noun3.capitalize()}{Fore.WHITE}.

This galaxy was a very dangerous one because it had
a {Fore.RED}Ruler{Fore.WHITE}, who hated {Fore.YELLOW}
the {noun2.capitalize()} galaxy{Fore.WHITE} and did what ever it takes to
destroy visitors from that galaxy.

As {Fore.YELLOW}{noun2.capitalize()}-masters{Fore.WHITE} were using {adj3}
{plural_noun(noun4)} to travel beyond {Fore.YELLOW}the {noun2.capitalize()}
galaxy{Fore.WHITE}, they {conjugate(verb2, tense = PAST)} with lots of power
as cosmos was a hostile environment for their {adj3} {plural_noun(noun4)}.

So the {Fore.RED}Ruler{Fore.WHITE} of {Fore.RED}the {noun3.capitalize()} galaxy
{Fore.WHITE} was always waiting for the
{adj3} {plural_noun(noun4)} to enter his territories.
As soon as he was informed that {choose_article(adj3, noun4)}
enters his galaxy, he ordered all of the living things in {Fore.RED}
the {noun3} galaxy{Fore.WHITE} to {verb1}.
It created the illusion for {Fore.YELLOW}{noun2.capitalize()}-
masters{Fore.WHITE} that they were entering their
own galaxy and they were stopping {verb_infinitive(verb2)} and as a
consequence - losing control of their {plural_noun(noun4)}.

Fortunately for the communication in the galaxy where {Fore.BLUE}{adj1} and
{adj2} {plural_noun(noun1)}{Fore.WHITE} were living,
it was not always the case, and thus, they were getting their
{plural_noun(noun3)} to chat with each other.

But once one of the {Fore.BLUE}{adj1} {plural_noun(noun1)}{Fore.WHITE} decided
to talk {Fore.YELLOW}{noun2.capitalize()}-masters{Fore.WHITE} into taking over
{Fore.RED}the {noun3.capitalize()} galaxy{Fore.WHITE} to make the recourses
for building their communication devices easier to obtain.
{Fore.BLUE}
"We have to make it easier for our folks to perform {verb_infinitive(verb1)}!
It is the most enjoyable activity for us!
We can't allow some greedy {Fore.RED}Ruler{Fore.WHITE} to take it from us!
Let's make more {adj3} {plural_noun(noun4)} and put more {noun1} in them that
we could travel beyond our galaxy all together!"
{Fore.YELLOW}
"We cannot let simple {Fore.BLUE}{noun1}{Fore.YELLOW} to go farther than
our terretory unprepared!
They have to learn their way to the appropriate status!
It is the low of our galaxy!"
{Fore.BLUE}
"I do know it!
But desperate times call for desperate measures!
We have to make an exception for the sake of our galaxy
and {plural_noun(noun1)} living here!"
{Fore.YELLOW}
"We have to take time to ponder it.
Let us think it through first cause it is all about the survival of our galaxy,
and {plural_noun(noun1)} as well."
{Fore.BLUE}
"That's what I'm talking about! Take your time, and call me after you come up
with your decision!"
{Fore.WHITE}
As {Fore.BLUE}{choose_article(adj1, noun1)}{Fore.WHITE} left the meeting,
{Fore.YELLOW}{noun2.capitalize()}-masters{Fore.WHITE} started their discussion.
There were plenty of arguments for and against taking over
{Fore.RED}the {noun3.capitalize()} galaxy{Fore.WHITE}. Some were insisting
that such an adventure may bring tremendous loses and tons of troubles rather
than unlimited resources of materials for {plural_noun(noun3)}. Others were
having conserns that it may also be quite costly to create so many
{adj3} {plural_noun(noun4)} for just a singe voyage. However, there were some
supporters of {Fore.BLUE}{choose_article(adj1, noun1)}{Fore.WHITE}'s idea,
and their main argument was that all these issues with obtaining materials
for {plural_noun(noun3)} were pretty exasperating since traveling to the same
hostile galaxy every now and then to get the materials was driving every one
up the wall. All this never ending {verb_infinitive(verb2)} while moving
on their {plural_noun(noun4)}. And even the fact that {Fore.RED}the Ruler
{Fore.WHITE} was misleading {Fore.YELLOW}{noun2.capitalize()}-masters
{Fore.WHITE} by using their own ritual of {verb_infinitive(verb1)}, which
had been passed from generation to generation in {Fore.YELLOW}
the {noun2.capitalize()} galaxy{Fore.WHITE}, was significantly unbearable for
everyone.

After all these debates, the {Fore.BLUE}{adj1} {noun1}{Fore.WHITE}'s
supporters {conjugate(verb1, tense = PAST)} and convinced the rest of
the masters to follow them. Although, the opposition had agreed, they presented
the supporters with an ultimatum. According to this ultimatum,
{Fore.BLUE}{choose_article(adj1, noun1)}{Fore.WHITE} should pass a special
text first to prove that {format_pronoun(noun1)} is worthy.

The {Fore.BLUE}{adj1} {noun1}{Fore.WHITE} was called to the masters to attend
the event that had been created to check if {format_pronoun(noun1)} was worthy.
He was given a list with some text and left alone in a small version of
{choose_article(adj2, noun4)}.
{Fore.BLUE}
"That's interesting and at the same time pretty engaging..."{Fore.WHITE}
- said the {Fore.BLUE}{adj1} {noun1}{Fore.WHITE} to
{formatting_reflexive_pronoun(noun1)} and started reading.

It was some kind of a quiz, which consisted five lines filled with words and
one empty line at the end:

1. {' '.join(idioms_list[1][0].lower().split( )[::-1])}
2. {' '.join(idioms_list[1][1].lower().split( )[::-1])}
3. {' '.join(idioms_list[1][2].lower().split( )[::-1])}
4. {' '.join(idioms_list[1][3].lower().split( )[::-1])}
5. {' '.join(idioms_list[0].lower().split( )[::-1])}
6. ______
{Fore.BLUE}
"Hmm...Looks like there are some phrases written in reverse order..."
{Fore.WHITE}
{format_pronoun(noun1).capitalize()} readjasted the content in his mind and
instead of a meanenless phrases, {format_pronoun(noun1)} got the meaningful
sentences instead:

1. {idioms_list[1][0]}
2. {idioms_list[1][1]}
3. {idioms_list[1][2]}
4. {idioms_list[1][3]}
5. {idioms_list[0]}
6. ______
{Fore.BLUE}
"Got it!"
{Fore.WHITE}
And {format_pronoun(noun1)} wrote a single sentence where the empty line was:
{idioms_dictionary.get(idioms_list[0])}.
After all he started {verb_infinitive(verb1)} to attract {Fore.YELLOW}
{noun2.capitalize()}-masters{Fore.WHITE}' attention. And it worked!
They entered the confined place where the {Fore.BLUE}{adj1}
{noun1}{Fore.WHITE} had stayed alone while solving a word puzzle.
They took the piece of paper and nodded in agreement.
Had it not been for the bright mind of the {Fore.BLUE}{adj1}
{noun1}{Fore.WHITE}, they would never have allowed him to participate in
their traveling. But the question was how to let the rest of unexperienced
{plural_noun(noun1)} to go with them.
{Fore.YELLOW}
"We will give you the green light! Go and insight the rest of our folks!
Teach them everything that you know! We will give you time for it.
Now leave."
{Fore.WHITE}
And {format_pronoun(adj1, noun1)} left while {verb_infinitive(verb1)}.
He was {verb_infinitive(verb1)} all {format_pronoun(noun1)} way back to
the rest of {plural_noun(noun1)}.
When all {plural_noun(noun1)} became aware of their nearest future, they
were over the moon! And the preparations had started!

All {Fore.YELLOW}the {noun2.capitalize()} galaxy{Fore.WHITE} were in real hurry
to get everything ready for their adventure into the space.
Each {adj1} {noun1} and each {adj2} {noun1} wanted to finish with limited
communication between each other. As chatting on {plural_noun(noun3)} and
{verb_infinitive(verb1)} were their favorite activities they were eager to
go for the invasion in {Fore.RED}the {noun3.capitalize()} galaxy
{Fore.WHITE}.

And when everything was ready such as enough amount of provision, and enough

    '''
    print(madlib_2)
