'''DOCUMENTATION
Created by @aftonsenpai - 05:23 AM | 19/12/24
Last Updated: 20:14 PM | 23/12/24
Type - Console Game
Title - Guess the Number
Version - 3.9.7
'''
from random import randint, choice
from os import system as s
from time import sleep

praises = ("You've won", "Nice game", "Great round", "Good job", "That was neat")


def simple_guess():
    rnum = randint(0,9)
    s('cls')
    print("Guess the Number [Simple Edition]")
    print("Rules: \n[#] You got three chances \n[#] Guess from 0 to 9")
    for i in range(3):
        gnum = int(input("Guess the number!: "))
        if gnum > rnum and gnum <= 9: 
            print("That's too high!"); k = 0
        elif gnum < rnum and gnum >= 0:
            print("That's too low!"); k = 0
        elif gnum > 9 or gnum < 0:
            print("That's out of range! Try again!")
        else:
            k = 1; break
    print("You Lose!") if k==0 else print("{}!".format(choice(praises)))


def oe_guess():
    rnum = randint(0,99)
    count = 5
    def last_chance():
        gnum = int(input("Guess the number!: "))
        if gnum > rnum and gnum < 100:
            print("That's too high.")
        elif gnum < rnum and gnum > 0:
            print("That's too low")
        elif gnum > 99 or gnum < 0:
            print("That's out of range! Pick a number between 0 and 99")
        else:
            return "WIN"
        return "LOSE"
    while True:
        if count == 0:
            if last_chance() == "WIN":
                print("{}!".format(choice(praises)))
            else:
                print("You Lose!")
            break
        else:
            gnum = int(input("Guess the number!: "))
            if gnum > rnum and gnum < 100:
                print("That's too high.\n",warning.format(count))
            elif gnum < rnum and gnum > 0:
                print("That's too low\n",warning.format(count))
            elif gnum > 99 or gnum < 0:
                print("That's out of range! Pick a number between 0 and 99")
            else:
                print("{}!".format(choice(praises)))
                break
        count -= 1

#WORK UNDER PROGRESS
#def ne_guess()

def menu(mode):
    def re(message, mode):
        print(message)
        sleep(0.8)
        s('cls')
        if mode == "m":
            menu("self")
        elif mode == "self":
            quit()
        else:
            return 0
    s('cls')
    print("Guess the Number [MENU]")
    print("[1] Simple Edition")
    print("[2] Original Edition")
    print("[3] New Edition")
    try:
        ch = int(input("[>] "))
        if ch == 1:
            simple_guess()
        elif ch == 2:
            oe_guess()
        elif ch == 3:
            re("Will be added soon", "m")
        elif ch == 0:
            re("You Quit", mode)
        else:
            re("Invalid Input", "m")
        sleep(1.2)
        s('cls')
        re("Thanks for Playing!","self")
    except ValueError:
        re("Invalid Input", "m")

if __name__ == "__main__":
    warning = "Remember! You've got only {} more lives left!"
    menu("self")
