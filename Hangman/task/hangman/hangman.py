# Write your code here
import random 

words = ['python', 'java', 'kotlin', 'javascript']
word_choice = list(random.choice(words))
word_set = set(word_choice)
current = list("-" * len(word_choice))
print("H A N G M A N\n")
for i in range(8):
    print(''.join(map(str, current)))
    guess = input("Input a letter:")
    start = 0
    if guess in word_set:
        for c in word_choice:
            if c == guess:
                index = word_choice.index(c, start)
                current[index] = guess
                start = index + 1
    else:
        print("No such letter in the word") 
    print("\n")
print("Thanks for playing!\nWe'll see how well you did in the next stage")
