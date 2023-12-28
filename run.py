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