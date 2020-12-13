# Write your code here
import random 

words = ['python', 'java', 'kotlin', 'javascript']
word_choice = random.choice(words)
hint = word_choice[0:3]
letters_left = len(word_choice) - 3
print("H A N G M A N")
guess = input("Guess the word {}: ".format(hint + ("-" * letters_left)))
if guess == word_choice:
    print("You survived!")
else:
    print("You are hanged!")
