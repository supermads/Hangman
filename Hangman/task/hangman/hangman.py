# Write your code here
import random 


def menu():
    print("H A N G M A N\n")
    choice = input('Type "play" to play the game, "exit" to quit:')
    if choice == "play":
        play_game()


def play_game():
    words = ['python', 'java', 'kotlin', 'javascript']
    word_choice = list(random.choice(words))
    word_set = set(word_choice)
    current = list("-" * len(word_choice))
    lives = 8
    keep_playing = True
    tries = []
    while lives > 0:
        if len(word_set) == 0:
            print("You guessed the word!\nYou survived!")
            keep_playing = False
            lives = 0
        if keep_playing:
            print("\n")
            print(''.join(map(str, current)))
            start = 0
            guess = input("Input a letter:")
            if guess in tries:
                print("You already typed this letter")
            elif len(guess) != 1:
                print("You should input a single letter")
            elif guess.isupper() or guess.isalpha() == False:
                print("It is not an ASCII lowercase letter")
            elif guess in word_choice:
                if guess in word_set:
                    for c in word_choice:
                        if c == guess:
                            index = word_choice.index(c, start)
                            current[index] = guess
                            start = index + 1
                    word_set.remove(guess)
                    tries.append(guess)
            else:
                print("No such letter in the word")
                tries.append(guess)
                lives -= 1
    if len(word_set) != 0:
        print("You are hanged!")
    menu()
    
    
menu()
