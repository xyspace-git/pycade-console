'''DOCUMENTATION
Created by @aftonsenpai - 05:23 AM | 19/12/24
Last Updated: 20:19 PM | 23/12/24
Type - Console Game
Title - Pycade Console
Version - 1.0.4
'''
def re(message, ctype):
    print(">>> {} <<<".format(message))
    sleep(0.6)
    s('cls')
    quit() if ctype == "q" else menu()

def menu():
    print("|~=~=~[PYCADE MINIGAMES]~=~=~|")
    print("[1] Guess the Number")
    print("[2] Quizzo")
    print("[3] Rock Paper Scissor")
    print("[4] Hangman")
    print("[5] Tic-Tac-Toe")
    try:
        ch = (input("[>] "))
        if ch == '1':
            import guess
            guess.menu("module")
        elif ch == '2':
            re("Will be added soon", "m")
        elif ch == '3':
            re("Will be added soon", "m")
        elif ch == '4':
            re("Will be added soon", "m")
        elif ch == '5':
            re("Will be added soon", "m")
        elif ch == 'q':
            re("You Quit", ch)
        else:
            re("Invalid Input", "m")
    except Exception:
        re("Invalid Input", "m") 

from os import system as s
from time import sleep
game = "RUN"
while True:
    menu()
