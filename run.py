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
                    You will have 7 chances to guess the random word by
                    entering a single character each guess.
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
        choice = input("Do you want play hangman again? (yes/no): ")
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

def start_hangman_game():

    """
    This function starts the game for the user. If a users input is incorrect 
    they will lose a chance to guess again. The user is also told if they
    have already guessed a letter and if they are trying to guess an invalid character.
    """
    
    welcome()
    word = get_random_word_from_wordlist()
    temp = get_some_letters(word)
    letters_guessed = []
    chances = 7
    found = False
    while True:
        if chances == 0:
            print(f"$Sorry! You Lost, the word was: {word}\n")

            print(f"""
            Better luck next time
            ======================""")
            break
        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"$Chances left: {chances}")
        character = input("$Enter the character you think the word may have: ")
        if len(character) > 1 or not character.isalpha():
            print("$Please enter a single alphabet only")
            continue
        elif character in letters_guessed:
            print('$You have already guessed that letter before.Try again!')
        elif character not in word:
                print('$Sorry, that letter is not part of the word.Try again!')
                letters_guessed.append(character)
        else:
            for num, char in enumerate(list(word)):
                if char == character:
                    templist = list(temp)
                    templist[num] = char
                    temp = ''.join(templist)
                    found = True
        if found:
            found = False
        else:
            chances -= 1
        if '_' not in temp:
            print(f"$\nYou Won! The word was: {word}")
            print(f"$You got it in {7 - chances} guess")
            break
        else:
            draw_hangman(chances)
        print()

#full program run    
start_hangman_game()
play_again()