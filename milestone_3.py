#%%
#Task1: check iteratively for the word
import random

word_list = ["apple", "banana", "orange", "pear", "peach"]
word = random.choice(word_list)

#step 1: check for validity of guessed letters
# Step 1
while True:
    # Step 2
    guess = input("Guess a letter: ")

    # Step 3
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        # Step 5
        print("Invalid letter. Please, enter a single alphabetical character.")

# Print the valid guess
print("Your guess is:", guess)
# %%
#Task 2: check whether guessed word in list
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:   
    print(f"Sorry, {guess} is not in the word. Try again.")

# %%
#define the function for the first task as check_guess
import random
word_list = word_list = ['banana', 'apple', 'orange', 'kiwi', 'mango']
word = random.choice(word_list)

def check_guess(guess):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:   
        print(f"Sorry, {guess} is not in the word. Try again.")

#ask for input function
#step 1: define the function
def ask_for_input():
    while True:
        guess = input('Please enter a single letter: ') #asks user for input 

        if len(guess) == 1 and guess.isalpha() is True:
            print('Good guess!: ', guess)
            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

#outside while but within function call check
    check_guess(guess)
#outside function call it
ask_for_input()

# %%
