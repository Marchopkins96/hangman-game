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


    