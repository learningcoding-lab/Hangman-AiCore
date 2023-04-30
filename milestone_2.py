#create a word list and print its output
word_list = ['banana', 'apple', 'orange', 'kiwi', 'mango']
print(word_list)

#import the function random
import random

#import the function random and its choice function
word = random.choice(word_list)

#print the final output
print(word)

#ask the user to enter a single letter
#assigning this input to guess
guess = input('Please enter a single letter: ')

#Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha() is True:
    print('Good Guess!')

else:
    print("Oops! That's not a valid input!")




