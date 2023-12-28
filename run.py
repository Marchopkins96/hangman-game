import random

#define a welcome function
def welcome():

    name = input("""
    
                ============================================================
                
                > Welcome to the Hangman Game! Please enter your game name:  <
                """).capitalize()

    if name.isalpha() == True:
        print(""">> Hi!""",name,"""Glad you could be here! <<<
                    You will be playing against the computer today.
                    The computer will randomly choose a word and 
                    you will have to try and guess what the word is!
                    
                    ==================================================
                    
                    Good Luck! Have fun playing :)))""")

    else:
        print('Please enter your name using letters only')
        name = input('Enter a game name here: ')
        print('Hi',name,'Please go through the rules of the game below')

#define a play again function
def play_again():

    """
    This function asks the user if they wish to play the game again
    """
    response = input("Would you like to play again? yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()
    reply = ('y', 'n')

    if response not in reply:
        print('Invalid Entry! Please check that you entered the correct input: ')
        response = input("Please enter the correct input here. Either yes/no. Enter 'Y' for Yes or 'N' for No: ").lower()

    else:
        if response == 'y':
            game_run()

        elif response == 'n':
            print('Hope you had fun playing the game! Come back soon!')

    
