import random

def get_random_word_from_wordlist():
    """
    This function generates a random word from the wordlist file
    """
    wordlist = []
    with open("wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word

def get_some_letters(word):
     """
    This function takes the randomly selected word as the parameter.
    A sequence of dashes (_) and some letters will be displayed to the user.
    """
    letters = []
    temp = '_'*len(word)
    for char in list(word):
        if char not in letters:
            letters.append(char)
    character = random.choice(letters)
    for num, char in enumerate(list(word)):
        if char == character:
            templist = list(temp)
            templist[num] = char
            temp = ''.join(templist)
    return temp

def getAvailableLetters(letters_guessed):
    #list of letters a guess can be
    alph = "abcdefghijklmnopqrstuvwxyz"
    r = ""
    for i in alph:
        if i not in lettersGuessed:
            r = r+i
    return(r)

def welcome():
    #This function welcomes the user to the game and asks for input from them
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


def play_again():
    """
    This function allows the user the option to play again if they wish
    """
    while True:
        choice = input("Do you wanna play hangman? (yes/no): ")
        if 'yes' in choice.lower():
            start_hangman_game()
        elif 'no' in choice.lower():
            print('Quitting the game...')
            break
        else:
            print("Please enter a valid choice.")
        print("\n")

#The following function stores the imagery for the hangman visual
def draw_hangman(chances):
    if chances == 6:
        print("________      ")
        print("|      |      ")
        print("|             ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 5:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|             ")
        print("|             ")
        print("|             ")
    elif chances == 4:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /       ")
        print("|             ")
        print("|             ")
    elif chances == 3:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|      ")
        print("|             ")
        print("|             ")
    elif chances == 2:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|             ")
        print("|             ")
    elif chances == 1:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     /       ")
        print("|             ")
    elif chances == 0:
        print("________      ")
        print("|      |      ")
        print("|      0      ")
        print("|     /|\     ")
        print("|     / \     ")
        print("|             ")