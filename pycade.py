
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

import guess
from os import system as s
from time import sleep
game = "RUN"
while True:
    menu()