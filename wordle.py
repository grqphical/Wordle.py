import random
from os import system

# Reads files from words.txt and creates a list of all 5 letter words
words = []
with open('words.txt', 'r') as f:
    for line in f:
        words.append(line.strip())

word = words[random.randint(0,len(words))]

# Game Class
class Wordle:
    def __init__(self):
        # The word to find
        self.word = str(word)
        # Number of guesses
        self.guesses = 0
        # Number of correct letters in the correct place
        self.correct_ones = 0
        # Valid words list
        self.words = words
    def mainloop(self):
        # Clears the screen and prints tht title
        system("cls")
        print("Wordle.py - Wordle made in python")
        running = True
        while running:
            if self.guesses < 6:
                # Checks if the person has guessed less than 6 times and prints a prompt
                guess = input(f"Guesses Left: {6 - self.guesses}> ")
                if len(guess) > 5:
                    # Too long of a word error
                    print("Error: Too long of a word")
                    continue
                elif len(guess) < 5:
                    # Too short of a word error
                    print("Error: Too short of a word")
                    continue
                # checks if word is valid by looking if it is in the word list if it isnt it will print an error
                elif not guess in self.words:
                    print("Error: Invalid Word")
                    continue
                # Word is valid continue game
                else:
                    for letter in guess:
                        # Loops through every letter 
                        # Checks if the letetr is in the word AND is in the righ tplace
                        if guess.find(letter) == self.word.find(letter):
                            # If it is print it with a green background and incriment the number of correct letters
                            new_letter = f"\033[0;37;42m{letter}\033[0;37;40m"
                            print(new_letter, end="")
                            self.correct_ones += 1
                        elif letter in self.word:
                            # If the letter is in the word but not in the right place it will be printed witha  yellow background
                            new_letter = f"\033[0;37;43m{letter}\033[0;37;40m"
                            print(new_letter, end="")                       
                        else:
                            # It will just print the letetr with no colour
                            print(letter, end="")
                    # Incriments the amount of guesses
                    self.guesses += 1
                print("\n")
                # If they have all 5 letters correct they win
                if self.correct_ones == 5:
                    print("You win!")
                    break
                # Resets game
                self.correct_ones = 0
            # If they run out of guesses they lose
            else:
                print(f"Too bad the wordle was: \033[1;37;40m{self.word}\033[0;37;40m")
                running = False
# Starts the app
if __name__ == '__main__':
    wordle = Wordle()
    wordle.mainloop()
