import random
words = ["apple", "banana", "pear", "berry", "mango", "papaya", "plum"]

def main():
    word = random.choice(words)
    progress = ["_"] * len(word)
    lives = 7
    
    while True:
        print(f"Remaining lives: {lives}")
        print(progress)
        guess = input("Guess a letter: ")
        if guess in word:
            correct_guess(guess, word, progress)
        else:
            lives -= 1
        
        if lives <= 0:
            print(f"No lives left.\nWord was {word}.")
            return
        elif "_" not in progress:
            print(f"You guessed it!\nThe word was {word}")
            return


def correct_guess(letter, word, progress):
    for x in range(len(word)):
        if letter == word[x]:
            progress[x] = letter

main()
