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