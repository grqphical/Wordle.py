import random
import colorama

words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

word = words[random.randint(0,len(words))]

class Wordle:
    def __init__(self):
        self.word = str(word)
        self.guesses = 0
        self.correct_ones = 0
        self.words = words
    def mainloop(self):
        print("Wordle.py - Wordle made in python")
        running = True
        while running:
            if self.guesses < 6:
                
                guess = input(f"Guesses Left: {6 - self.guesses}> ")
                if len(guess) > 5:
                    print("Error: Too long of a word")
                    continue
                elif len(guess) < 5:
                    print("Error: Too short of a word")
                    continue
                elif not guess in self.words:
                    print("Error: Invalid Word")
                    continue
                else:
                    for letter in guess:
                        if guess.find(letter) == self.word.find(letter):
                            new_letter = f"\033[0;32;40m{letter}\033[0;37;40m"
                            print(new_letter, end="")
                            self.correct_ones += 1
                        elif letter in self.word:
                            new_letter = f"\033[0;33;40m{letter}\033[0;37;40m"
                            print(new_letter, end="")
                        
                        else:
                            print(letter, end="")
                    self.guesses += 1
                print("\n")
                if self.correct_ones == 5:
                    print("You win!")
                    break
                self.correct_ones = 0
            else:
                print(f"Too bad the wordle was \033[1;37;40m{self.word}")
                running = False

wordle = Wordle()
wordle.mainloop()