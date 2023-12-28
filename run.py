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

def get_word():
    """
    This function generates the word from 'wordlist.txt' that the user will attempt to guess.
    """
    wordlist = []
    with open("wordlist.txt", 'r') as file:
        wordlist = file.read().split('\n')
    word = random.choice(wordlist)
    return word

def play_game():
    #call the welcome function
    welcome()

    alphabet = ('abcdefghijklmnopqrstuvwxyz')

    #This will generate the random word for the user
    word = get_word()

    #Empty list for guessed letters
    letters_guessed = []

    #Number of tries the user is allowed in the game
    tries = 7

    guessed = False

    print()

    #print a guess hint for the user for number of letters in the the word
    print('The word contains', len(word), 'letters.')
    print(len(word) * '_')

    #This is a while loop that takes into consideration if the user is guessing a letter or guessing a whole word.
    #It also informs the user if they input a wrong guess and if the inputted amount of letters is equal to the length of the word(if guessing whole words).
    while not guessed and tries > 0:
        print('You have ' + str(tries) + ' tries')
        guess = input('Guess a letter you think is in the word or enter the full word if you are feeling brave!').lower()
        #By this point the user has inputted a guess

        if len(guess) == 1:
            if guess not in alphabet:
                print('Please make sure that you enter a letter of the alphabet')
            elif guess in letters_guessed: 
                print('You have already guessed that letter! Guess again!')
            elif guess not in word:
                print('Sorry, that letter is not part of the word.')
                letters_guessed.append(guess)
                tries -=1
            elif guess in word:
                print('Great! That letter is in the word! keep going!!')
                letters_guessed.append(guess)
            else:
                print('check your entry! It must be a letter...')

        #if a user wants to attempt to guess a full word
        elif len(guess) == len(word):
            if guess == word:
                print('Wow! You guessed the word correctly!')
                print('The word is: ', word)
                guessed = True
            else:
                print('Sorry, that\'s not the word!')
                print('the correct word was: ', word)
                tries -=1
        
        #user input letters is not equal to the total number of letters in the word to guess
        else:
            print('The length of your guess does not match the length of the correct word.')
            tries -=1

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '_'

            #this piece of code above is for displaying the hangman image
            #function for it displaying shown below
            print(hangman(tries))
            print(status)

        if status == word:
            print('Great Job! You guessed the word correctly!')
            guessed = True
        elif tries == 0:
            print("Uh Oh! You are out of guesses and you have not got the word!")
            print('The correct word was: ', word)

    #call play_again function if user wishes to do so
    play_again()

    #This function displays the hangman image to the user

    def hangman(tries):
        stages = [  """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]
#Full program run
play_game()()