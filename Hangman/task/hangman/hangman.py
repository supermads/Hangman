# Write your code here
import random 

words = ['python', 'java', 'kotlin', 'javascript']
word_choice = random.choice(words)
print("H A N G M A N")
guess = input("Guess the word: ")
if guess == word_choice:
    print("You survived!")
else:
    print("You are hanged!")
