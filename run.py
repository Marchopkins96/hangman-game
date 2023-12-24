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

def start_hangman_game():
    """
    This function defines the main logic of the program
    """
    word = get_random_words_from_wordlist()
    temp = get_some_letters(word)
    chances = 7
    found = False

    """
    This loop terminates when the user guesses the word correctly or runs out of chances.
    Begin the game by displaying the sequence, the number of letters in the word,
    and the chances left. User choice will be validated to check a character is
    in the alphabet.
    """
    """
    If there are no blank dashes left, display that the
    user won along with the number of guesses taken otherwise
    display the hangman in relation to the amount of chances left.
    """
    while True:
        if chances == 0:
            print(f"Sorry! You Lost, the word was: {word}")
            print("Better luck next time!")
            break

        print("=== Guess the word ===")
        print(temp, end='')
        print(f"\t(word has {len(word)} letters)")
        print(f"Chances left: {chances}")
        character = input("Enter the character you think the word may have: ")

        if len(character) > 1 or not character.isalpha():
            print("Please enter a single alphabet only")
            continue
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
            print(f"\nYou Won! The word was: {word}")
            print(f"You got it in {7 - chances} guess")
            break
        else:
            draw_hangman(chances)

        print()

