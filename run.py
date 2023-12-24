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

