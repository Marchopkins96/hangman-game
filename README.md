# Hangman Game
(Developed by: Marc Hopkins)

![Responsive](docs/iamresponsive.png)

[Live webpage](https://hangman-game-tuti.onrender.com/)

## Introduction 

The Hangman Game is a word guessing game in which a user plays against the computer program to try and guess a random word within a certain amount of guesses.

## How to play 

Hangman is a guessing game for two players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses. 

In this version a user is prompted to enter their game name, once they have done this a short instruction list will display before then being asked to input a guess. The random word will be displayed as some letters and dashes (w_r_). If the user guesses correct a dash will be replaced with a letter and if a wrong letter is chosen more parts of the hangman image will display. A user will win if they get the word within the set amount of guesses and they lose if they run out of guesses and the whole hangman image is displayed on screen.

## Project Goals 

### User Goals
- The site's user wants to play an online hangman game in which they are tested and have fun in the proccess.

### Site Owner Goals
- The Site owner's goal is to provide a fun version of a family classic game which a user can enjoy with friends and family.

## User Experience 

### Strategy

#### Target Audience
- Users with an interest in guessing games
- Users looking for entertaing online content.

#### User Requirements and Expectations
- Simple navigation around game
- Immediate feedback on progress throughout game
- Accessibility

#### User Stories

##### Game Users
As a game user, I want to ...
1. ... easily navigate through the game.
2. ... get clear feedback whilst playing.
3. ... easily return to the beginning of the game and play again.

##### Game owner
As the game owner, I want to ...
1. ... interact with the game, stay engaged and be challenged.

### Scope 

#### Initial Stage

At the initial stage the game will present a welcome message and invite a user to enter their name, then display short instructions before a guess can be made by the user. If a user guesses the word with a set amount of guesses they are informed they won and if not they are told that they lose. At the end of a game the user can choose to play again or not.

#### Future Additions 

In the future it would enhance the experience of the game if the user had a choice of level that they could pick. Each level would include different lengths of words designed to test the user based on their ability and provide more of a challenge.

### Game Features

#### Welcome to the game 

<details>
<summary>Screenshot of Welcome to game section</summary>
<img src="docs/startofgame.png" width="700">
</details>

- Features a welcome message and invites a user to input a game name.

#### Instructions 

<details>
<summary>Screenshot of instructions</summary>
<img src="docs/instructions.png" width="700">
</details>

- When a name is inputted then the instructions show and wish the user good luck. Further down the screen a user can input their guess.

#### User name saved 

<details>
<summary>Screenshot of saved user name</summary>
<img src="docs/namesave.png" width="700">
</details>
 
- The users name is saved when they input it. This makes the game more personal for users.

#### Correct letter input

<details>
<summary>Screenshot of correct letter feedback</summary>
<img src="docs/correctletter.png" width="700">
</details>

- The user recieves instant feedback when a character that is in the random word is inputted.

#### Wrong letter input

<details>
<summary>Screenshot of wrong letter feedback</summary>
<img src="docs/wrongletter.png" width="700">
</details>

- The user recieves instant feedback when a character that isnt in the random word is inputted.
- This happens in the form of a textual message and the hangman image parts appearing.

#### Lost Game

<details>
<summary>Screenshot of a lost game</summary>
<img src="docs/playagain.png" width="700">
</details>

- The user is told they lose the game and the full hangman is presented on screen.
- The option to play again is available to the user.

#### Won Game

<details>
<summary>Screenshot of a Winning game</summary>
<img src="docs/youwon.png" width="700">
</details>

- The user is told they won the game and that isstantly ends the game loop.
- The option to play again is again presnted to the user.

#### Restart Game

<details>
<summary>Screenshot of a restarted game</summary>
<img src="docs/restartgame.png" width="700">
</details>

- If a user chooses the yes option they are taken back to the very start of the game so they can play again.

#### Quit Game

<details>
<summary>Screenshot of a quit game</summary>
<img src="docs/quitgame.png" width="700">
</details>

- If the user chooses the no option they quit the game and a message is presented on screen to tell the user.

## Technologies Used

### Languages
- Python

### Tools 
- Git
- Github
- Render

### Helpful sites

A few sites came in handy when developing my own version of this game:

- <a href="https://www.w3schools.com/">W3 Schools</a>
- <a href="https://gist.github.com/">GitHub Gist<a>

## Testing and Validation

### PEP8 CI Python Linter

- No errors are flagged when testing the python code from run.py in the PEP8 CI Python Linter.

![Python Testing](docs/pythonlinter.png)

### Manual Testing

I have manually tested this project by doing the following:
- Entering numbers as input when the program is expecting letters.
- Entering more than one letter as a users guess.

Both of the above tests return the developers desired result.
- The game has been tested in the local terminal as well as the Render terminal.

#### Outstanding Issues 

There are currently no outstanading issues at this time to the developers knowledge.

### Testing User Stories

** As a game user, I want to ...**
1. ... Be able to enter a game name.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Enter game name | Game name is saved and the game loads | Works as expected |

2. ... Read how to play the game.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Press enter after entering game name | user is welcomed to game and instructions on how to play are shown | Works as expected |

3. ... Easily submit a guess in the game.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Enter guess after 'Enter the character you think the word may have' and press enter | guess is submitted and the program tells a user if the guess is in the word or not | Works as expected |

4. ... See progress throughout game.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | A user enters a guess | After each guess a user takes it will either be part of the random word to guess or it will not and the hangman image will display more parts each time a wrong guess is submitted | Works as expected | 

5. ... Be able to play again.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Press 'yes' to 'Do you want to play again' | User is taken back to the very start of the game and can play again | Works as expected | 

6. ... Be able to quit the game.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Press 'no' to 'Do you want to play again' | The game is quit in the terminal and a message is presented to the user to tell them | Works as expected |


** As the game owner, I want to ...**
1. ...Create a game that is easy to use.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | Enter guesses | Guesses are executed and game goes through motions | Works as expected |

2. ...Provide instructions for the game.

| **Feature** | **Action** | **Expected result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Terminal | enter game name | Instructions display with welcome message | Works as expected |

## Bugs and Fixes

| **Bug** | **Fix** |
| -------------- | -------------- |
| When running my code through the CI Python Linter Validator a number of 'Invalid escape sequence \ errors flagged up. These errors related to the code within function draw_hangman() which stores the code for the hangman imagery that is displayed in the game terminal. | In order to fix these errors an additional \ was added after each \ in this function to fix the issue and eliminate the errors. |

## Deployment & Development 

This project was deployed on Render. The instructions provided on Slack channel 'render' were used to ensure this project was deployed correctly and that all correct steps were taken. 
The link to these instructions on how to deploy on Render are as follows:
- <a href="https://code-institute-students.github.io/deployment-docs/10-pp3/pp3-01-web-service-creation">Render Deployment<a>

The project can be forked by the following steps:

1. Go to the GitHub repository.
2. Click on the fork button in the upper right hand corner.

The repository can be cloned by the following steps:

1. Got to the GitHub repository.
2. Locade the Code button above the list of files and click on it.
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
4. Open Git Bash.
5. Change the current working directory to the one where you want the cloned directory.
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7. Press Enter to create your local clone.

## Credits 

### Code 

Resources and insiration came from the following sources:

- The layout and set up of the game were modelled on a couple of different code sources that i found on GitHub.
- These sources helped me visualise what the game could look like and what features it should include.

The code sources are as follows:
- [Code Inspiration](https://github.com/Prithivee7/Hangman/blob/main/play_hangman.py)
- [Code Insiration 2](https://github.com/makeuseofcode/Hangman-Game/blob/main/hangman.py)

### Acknowledgements 

I would like to thank:

- My mentor Mitko Bachvarov for his Feedback, advice and guidance throughout this project.
- Members of the Slack community who answered my questions & queries.
- My partner, Harriet, for her feedback and encouragement throughout.





