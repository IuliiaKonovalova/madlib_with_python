import os
from colorama import Fore, Style
from simple_term_menu import TerminalMenu
from time import sleep
from madlibs import main_madlib, main_madlib_2


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
    options = ['1. Learn the rules', '2. Play the game', '3. Quit']
    main_menu = TerminalMenu(options)
    sub_options = [
        '1. Story 1: "Absolute Madness"',
        '2. Story 2: "Slight Madness"',
        '3. Go back']
    sub_menu = TerminalMenu(sub_options)
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
            suboptions_index = sub_menu.show()
            suboptions_choice = sub_options[suboptions_index]
            message_to_user_1 = f'''
    {Fore.GREEN}Be ready to type words...
                '''
            message_to_user_2 = f'''
    {Fore.GREEN}The end.{Fore.WHITE}{Style.RESET_ALL}
                '''
            if suboptions_choice == '1. Story 1: "Absolute Madness"':
                print(message_to_user_1)
                sleep(1)
                main_madlib()
                sleep(1)
                print(message_to_user_2)
            elif suboptions_choice == '2. Story 2: "Slight Madness"':
                print(message_to_user_1)
                sleep(1)
                main_madlib_2()
                sleep(1)
                print(message_to_user_2)
            else:
                options_index = main_menu.show()

main()
