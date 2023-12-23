import random 

def get_random_words_from_wordlist():
    """
    Picks the random word from the 
    wordlist.txt file for the game
    """
    wordlist = []

    with open("wordlist.txt", 'r') as file:
        wordlist = file.read().split("\n")

    word = random.choice(wordlist)

    return word

def get_some_letters(word):
    """
    This function takes the randomly selected word as the parameter.
    A sequence of dashes (_) and some letters will be displayed to the user.
    """
    letters = []
    temp = '_' * len(word)

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