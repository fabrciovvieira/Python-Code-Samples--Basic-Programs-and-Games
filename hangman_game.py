# Hangman Game

import random

# List of words
word_list = ["apple", "banana", "cherry", "orange", "grape", "lemon", "pear", "kiwi", "melon", "mango", "bottle"]

# Option to start the game
option = input('Start a new game:\n[Y]yes\n[N]no\n=> ').upper()

# Secret word
secret_word = random.choice(word_list)
if option == 'Y':
    print('WELCOME TO THE HANGMAN GAME')
    # Number of attempts
    num_attempts = int(input('How many attempts do you want: '))

# Initializing variables
attempt = 0
correct_letters = []
wrong_letters = []
wrong_words = []

while True:
    game_option = input('\nGuess word [1]\nGuess letter [2]\n=> ')
    if game_option == '2':
        letter = input('\nEnter a letter: ').lower()
        # Check if the letter is in the secret word
        if letter in secret_word:
            correct_letters.append(letter)
        else:
            wrong_letters.append(letter)
            print("Wrong! That letter is not in the word.")
        attempt += 1
        print(f'Attempts used: {attempt}/{num_attempts}')

    elif game_option == '1':
        word_attempted = input('\nEnter a word: ').lower()
        if word_attempted == secret_word:
            print(f'\nCongratulations, you guessed the word {secret_word}')
            break
        elif word_attempted != secret_word:
            print('\nWrong word!')
            wrong_words.append(word_attempted)
            attempt += 1
            print(f'Attempts used: {attempt}/{num_attempts}')

    # Display the secret word with hidden letters
    hidden_word = ''
    for letter in secret_word:
        if letter in correct_letters:
            hidden_word += letter
        else:
            hidden_word += ' _ '
    print('\nWord: ' + hidden_word)
    print('Wrong letters: ' + ', '.join(wrong_letters))
    print('Wrong words: ' + ', '.join(wrong_words))
    print(f'Attempts used: {attempt}/{num_attempts}')

    if hidden_word == secret_word:
        print(f'\nCongratulations, you guessed the word {secret_word}')
        break
    elif attempt == num_attempts:
        print(f'\nYou have run out of attempts: {num_attempts}/{num_attempts}. The word was {secret_word}')
        break
