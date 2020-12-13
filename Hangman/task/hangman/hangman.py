# Write your code here
import random 

words = ['python', 'java', 'kotlin', 'javascript']
word_choice = list(random.choice(words))
word_set = set(word_choice)
current = list("-" * len(word_choice))
lives = 8
keep_playing = True
print("H A N G M A N\n")
while lives > 0:
    if len(word_set) == 0:
        print("You guessed the word!\nYou survived!")
        keep_playing = False
        lives = 0
    if keep_playing:
        print("\n")
        print(''.join(map(str, current)))
        guess = input("Input a letter:")
        start = 0
        if guess in word_choice:
            if guess in word_set:
                for c in word_choice:
                    if c == guess:
                        index = word_choice.index(c, start)
                        current[index] = guess
                        start = index + 1
                word_set.remove(guess)
            else:
                print("No improvements")
                lives -= 1
        else:
            print("No such letter in the word")
            lives -= 1
if len(word_set) != 0:
    print("You are hanged!")
