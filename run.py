import random 

hang = ["""
H A N G M A N - 

   +---+
   |   |
       |
       |
       |
       |
=========""", """
H A N G M A N - 

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
H A N G M A N - 

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
H A N G M A N - 

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
H A N G M A N -

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
H A N G M A N - 

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
H A N G M A N - 

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def get_random_word_list():
    """
    Picks the random word from the 
    wordlist.txt file for the game
    """
    wordlist = []

    with open("wordlist.txt", 'r') as file:
        wordlist = file.read().split("\n")

    word = random.choice(wordlist)

    return word

def displayBoard(hang, missedLetters, correctLetters, secretWord):
    print(hang[len(missedLetters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print("\n")

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):   #replace blanks with correctly guessed letter
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:  #show the secret word with spaces in between each letter
        print(letter, end=' ')

def getGuess(alreadyGuessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again!')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter.')
        else:
            return guess

def playAgain():
   return input("\nDo you want to play again? (y/n)").lower().startswith('y')

missedLetters = ''
correctLetters = ''
secretWord = get_random_word_list()
gameIsDone = False

while True:
    displayBoard(hang, missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('\nYes! The secret word is "' +
            secretWord + '"! You have won!')
            gameIsDone = True
    
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(hang) - 1:
            displayBoard(hang, missedLetters, 
            correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' 
            + str(len(correctLetters)) + ' correct guesses, the word was "'
            + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = get_random_word_list()
        else: 
            break
