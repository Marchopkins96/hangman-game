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
    When the random letter is found it will replace a blank dash.
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

def draw_hangman(chances):
    """
    This function draws out thr figure of the hangman. 
    As the number of chances keeps on decreasing, the more of the figure that will show.
    """
    if chances == 6:
        print("________ ")
        print("| | ")
        print("| ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 5:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| ")
        print("| ")
        print("| ")
    elif chances == 4:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| / ")
        print("| ")
        print("| ")
    elif chances == 3:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /| ")
        print("| ")
        print("| ")
    elif chances == 2:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| ")
        print("| ")
    elif chances == 1:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / ")
        print("| ")
    elif chances == 0:
        print("________ ")
        print("| | ")
        print("| 0 ")
        print("| /|\ ")
        print("| / \ ")
        print("| ")