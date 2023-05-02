#%%
# Step 1
word_list = ["apple", "banana", "orange", "mango", "pineapple"]

# Step 3
print(word_list)

# %%
# Step 1
import random

# Step 2
fruits = ["apple", "banana", "orange", "mango", "pineapple"]

# Step 3
word = random.choice(fruits)

# Step 4
print(word)
# %%
# Step 1
import random

# Step 2
fruits = ["apple", "banana", "orange", "mango", "pineapple"]

# Step 3
word = random.choice(fruits)

# Step 4
guess = input("Guess a fruit: ")

# Step 5
print("The random fruit was:", word)
print("Your guess was:", guess)
# %%
# Step 1
import random

# Step 2
fruits = ["apple", "banana", "orange", "mango", "pineapple"]

# Step 3
word = random.choice(fruits)

# Step 4
guess = input("Guess a fruit: ")

# Step 5
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

print("The random fruit was:", word)
print("Your guess was:", guess)
