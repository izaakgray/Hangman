import json
import random

wordList = json.load(open('wordlist.json'))
word = random.choice(wordList)

print('A word has been selected, please guess a letter!')

letters = len(word)
lives = 10

print('Letters: ', letters)
print('Lives remaining', lives)

while lives != 0 and letters != 0:
    guess = str(input('Guess: '))
    if len(guess) == 1:
        print('Do something')

    else:
        print('Please only enter a single letter.')


    if guess in word:
        print('Correct guess!')
        letters = letters - 1

    elif guess not in word:
        lives = lives - 1
        print('Incorrect guess. You have ', lives,' lives remaining.')