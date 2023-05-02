# Hangman-AiCore Project

This is a command-line implementation of the classic Hangman game in Python. The program generates a random word from a list of words, and the user must guess the letters in the word one at a time. The user has a limited number of guesses, and each incorrect guess results in the drawing of a new part of a hangman figure. If the user guesses all the letters in the word before running out of guesses, they win the game. Otherwise, the hangman figure is fully drawn, and the user loses the game.
Hangman Game


## Getting Started
Clone this repository to your local machine.
1. Install Python 3 on your machine, if it is not already installed.
2. Open your terminal or command prompt and navigate to the directory containing the repository.
3. Run the command python milestone_3.py to start the game.

## How to Play
1. The computer will generate a random word.
2. The player will have to guess the letters in the word one at a time.
3. The player has 6 attempts to guess the word correctly, otherwise the game is over.
4. The player will be shown a series of dashes representing the letters in the word. The dashes will be replaced with the correctly guessed letters as they are guessed.
5. If the player guesses a letter that is not in the word, they will lose an attempt.
6. If the player guesses a letter that is in the word, they will be informed and the corresponding dashes will be replaced with the letter.
7. If the player correctly guesses the entire word before running out of attempts, they win the game.

# Milestone 2: Variables for the game was created
The python file, milestone_2.py was created for this task. This consisted of 4 main tasks broken down. For task 1 and 2, initially we defined a list of words for the game and imported the random module and its .choice() function/method to draw out a randomly generated word from the list. This was then assigned to a variable called 'word'. 

```python
import random
word_list = word_list = ['banana', 'apple', 'orange', 'kiwi', 'mango']
word = random.choice(word_list)
print(word)
```

For Task 3 and 4, a new user input was created and the validity of each of these guesses were compared to check they are present in the word_list.

      while True:
          guess = input('Please enter a single letter: ') #asks user for input 

          if len(guess) == 1 and guess.isalpha() is True:
            print('Good guess!: ', guess)
            break

          else:
            print("Invalid letter. Please, enter a single alphabetical character.")


## How to Contribute
If you would like to contribute to this project, feel free to fork this repository and submit a pull request. Please make sure to write clear and concise commit messages and comments in your code.
