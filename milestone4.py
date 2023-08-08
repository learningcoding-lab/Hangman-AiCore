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
                self.list_of_guesses.append(guess)
                self.check_guess(guess) #check and call the guess method
                break
           
        return guess
        
        """ 
        If the guess is a single alphabetical character and it's not already in the list_of_guesses:
        Create an else block and call the check_guess method. 
        Remember to pass the guess as an argument to this method. 
        """

    def __init__ (self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = print(random.choice(self.word_list))
        self.word_guessed = ['' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    """ TASK 3: Return to your check_guess method and extend it to replace the underscore(s) in the word_guessed with the letter guessed by the user.
    In the if block of your check_guess method, after your print statement, do the following: 
    Create a for-loop that will loop through each letter in the word.
    Within the for-loop, do the following:
    1. Create an <code>if</code> statement that checks if the letter is equal to the guess.
    2. In the <code>if</code> block, replace the corresponding "_" in the <code>word_guessed</code> with the guess. 
    HINT: You can index the <code>word_guessed</code> at the position  of the letter and assign it to the letter """
    
    def check_guess(self, guess):
        guess = guess.lower()  #consistency of letter inputs
        if guess in self.word: #to find if the guessed letter is in the word
            print(f"Good guess! {guess} is in the word!") 
            # creates an iterator that produces pairs of index (i) and value (letter) for each character in self.word
            for i, letter in enumerate(self.word):
                    if letter == guess: #if the character(letter) in word matched the guess
                        self.word_guessed[i] = guess #replaced the blank in that index with guessed letter
            self.num_lives -= 1
        else:
            print("Sorry, wrong guess! Try again!")

    """ TASK 4: Define what happens if the guess is not in the word you are trying to guess.
    Step 1. In the check_guess method, Create an else statement.
    Step 2: Within the else block:
    Reduce `num_lives' by 1.
    print a message saying "Sorry, {letter} is not in the word."
    print another message saying "You have {num_lives} lives left."
    """
    def check_guess(self, guess):
        guess = guess.lower()  #consistency of letter inputs
        if guess in self.word: #to find if the guessed letter is in the word
            print(f"Good guess! {guess} is in the word!") 
            # creates an iterator that produces pairs of index (i) and value (letter) for each character in self.word
            for i, letter in enumerate(self.word):
                    if letter == guess: #if the character(letter) in word matched the guess
                        self.word_guessed[i] = guess #replaced the blank in that index with guessed letter
            self.num_lives -= 1
        else:
            self.num_lives -=1
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} left!")

#Test the hangman game
# Test the Hangman game
if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "orange", "grape", "watermelon"]
    hangman_game = Hangman(word_list)

    while True:
        user_guess = hangman_game.ask_for_input()
        print(f"Word guessed: {' '.join(hangman_game.word_guessed)}")
        print(f"List of guesses: {hangman_game.list_of_guesses}")

        if hangman_game.num_lives == 0:
            print("Game over! You're out of lives.")
            break
        elif all(letter != '' for letter in hangman_game.word_guessed):
            print("Congratulations! You've guessed the word!")
            break
