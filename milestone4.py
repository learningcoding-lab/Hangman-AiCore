import random

class Hangman():

    def __init__ (self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        """
        word: The word to be guessed, picked randomly from the word_list. Remember to import the random module into your script.
        """
        self.word = print(random.choice(self.word_list))
        """
        word_guessed: list - A list of the letters of the word, with for each letter not yet guessed. 
        For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. 
        If the player guesses 'a', the list would be ['a', '', '', '', ''].
        """
        self.word_guessed = ['' for _ in self.word]

        """
        num_letters: int - The number of UNIQUE letters in the word that have not been guessed yet.
        """

        self.num_letters = len(set(self.word))

        """ num_lives: int - The number of lives the player has at the start of the game. """

        self.list_of_guesses = []

    """ 
    Remember that a method is a function that is defined inside a class.
    Let's create the check_guess method.

    Step 1: Define a method called check_guess. 
    Pass the guess to the method as a parameter. 
    In the body of the method, write the code for the following steps:
    Convert the guessed letter to lower case
    Create an if statement that checks if the guess is in the word
    In the body of the if statement, print a message saying "Good guess! {guess} is in the word. 
    """

    def check_guess(self, guess):
        guess = guess.lower()  # Convert the guessed letter to lower case
        if guess in self.word:
            print(f"Good guess! {guess} is in the word!")
        else:
            print("Sorry, wrong guess! Try again!")

    """
    For now, let's create the ask_for_input method.
    Step 2. define a method called ask_for_input. In the body of the method, do the following:
    Create a while loop and set the condition to True.

    Ask the user to guess a letter and assign this to a variable called guess.
    Create an if statement that runs if the guess is NOT a single alphabetical character.
    In the body of the if statement, print a message saying "Invalid letter. Please, enter a single alphabetical character."
    Create an elif statement that checks if the guess is already in the list_of_guesses.
    In the body of the elif statement, print a message saying "You already tried that letter!".
    """

    def ask_for_input(self):
        while True:
           guess = input("Guess a letter: ").lower()
           
           if not guess.isalpha() or len(guess) != 1:
               print("Invalid letter. Please, enter a single alphabetical character.")
           elif guess in self.list_of_guesses:
               print("You already tried that letter!")
               
           else:
                self.check_guess(guess) #check and call the guess method
                break
           
        return guess
        
        """ 
        If the guess is a single alphabetical character and it's not already in the list_of_guesses:
        Create an else block and call the check_guess method. 
        Remember to pass the guess as an argument to this method. 
        """
#Test the hangman game
if __name__ == "__main":
    word_list = ["apple", "banana", "cherry", "orange", "grape", "watermelon"]
    hangman_game = Hangman(word_list)
    print(f"Word to guess: {hangman_game.word}")
    print(f"Word guessed: {hangman_game.word_guessed}")
    print(f"Number of unique letters: {hangman_game.num_letters}")
    print(f"Number of lives: {hangman_game.num_lives}")
    print(f"List of guesses: {hangman_game.list_of_guesses}")

    user_guess = hangman_game.ask_for_input()
    print(f"You guessed: {user_guess}")



