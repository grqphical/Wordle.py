import random
import colorama

words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line)

word = words[random.randint(0,0)]

class Wordle:
    def __init__(self):
        self.word = str(word)
        self.guesses = 0
        self.correct_ones = 0
    def mainloop(self):
        print("Wordle.py - Wordle made in python")
        running = True
        while running:
            if self.correct_ones == 5:
                print("You win!")
                break
            if self.guesses < 6:
                guess = input("Try to guess the Wordle!")
                if len(guess) > 5:
                    print("Error: Too long of a word")
                elif len(guess) < 5:
                    print("Error: Too short of a word")
                for letter in guess:
                    if guess.index(letter) == self.word.index(letter):
                        new_letter = f"\033[0;32;40m{letter}\033[0;37;40m"
                        print(new_letter, end="")
                        self.correct_ones += 1
                    elif letter in self.word:
                        new_letter = f"\033[0;33;40m{letter}\033[0;37;40m"
                        print(new_letter, end="")
                    
                    else:
                        print(letter, end="")
                print("\n")

wordle = Wordle()
wordle.mainloop()