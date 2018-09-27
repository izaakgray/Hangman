print('A word has been selected, please guess a letter!')

guessedLetter = str(input())

if len(guessedLetter) == 1:
    print('Do code')
else:
    print('Please only enter a single letter.')
    guessedLetter = str(input())


