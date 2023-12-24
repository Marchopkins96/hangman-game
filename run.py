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

