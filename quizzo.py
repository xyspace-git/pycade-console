'''
Created by @aftonsenpai - HH:MM AM/PM | DD/MM/YY
Type - Console Game
Title - Quizzo [Simple Edition]
Version - 1.0.x
'''

'''
DOCUMENTATION
Created by @aftonsenpai - 05:23 AM | 19/12/24
Last Updated: 02:17 AM | 04/05/25
Type - Console Game
Title - Pycade Console
Version - 2.0.0
'''

import random

def get_word():
    words = ['python', 'console', 'arcade', 'hangman', 'gameplay', 'debug', 'variable']
    return random.choice(words).upper()

def show_hang(tries):
    art = [
        '''
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        =========
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        =========
        '''
    ]
    return art[tries]

def play(word):
    chars = set(word)
    used = set()
    tries = 6
    board = ["_" for _ in word]

    print("Welcome to Pycade Console - Hangman!\n")
    print(show_hang(tries))
    print("Word:", " ".join(board), "\n")

    while tries > 0 and set(board) != chars:
        g = input("Guess a letter: ").upper()
        if not g.isalpha() or len(g) != 1:
            print("Enter one letter.\n")
            continue
        if g in used:
            print("Already guessed that.\n")
            continue

        used.add(g)

        if g in chars:
            for i, c in enumerate(word):
                if c == g:
                    board[i] = g
            print("✅ Nice!")
        else:
            tries -= 1
            print(f"❌ Nope. Tries left: {tries}")

        print(show_hang(tries))
        print("Word:", " ".join(board), "\n")

    if set(board) == chars:
        print(f"🎉 You got it! Word was: {word}")
    else:
        print(f"💀 Out of tries. Word was: {word}")

def main():
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()
