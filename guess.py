'''
Created by @aftonsenpai - 05:23 AM | 19/12/24
Type - Console Game
Title - Guess the Number [Simple Edition]
Version - 1.0.4
'''
from random import randint, choice
from os import system as s
s('cls')
praises = ("You've won", "Nice game", "Great round", "Good job", "That was neat")

def simple_guess():
    rnum = randint(0,9)
    print("Guess the Number [Simple Edition]")
    print("Rules: \n[#] You got three chances \n[#] Guess from 0 to 9")
    for i in range(3):
        gnum = int(input("Guess the number!: "))
        if gnum > rnum: 
            print("That's too high!"); k = 0
        elif gnum < rnum:
            print("That's too low!"); k = 0
        elif gnum > 9 or gnum < 0:
            print("That's out of range! Try again!")
        else:
            k = 1; break
    print("You Lose!") if k==0 else print("{}!".format(choice(praises)))
    return "Thanks for playing!"

simple_guess()





















warning = "Remember! You've got only {} more lives left!"
def fun_guess(chances):
    rnum = randint(0,99)
    for count in range(chances,0,-1):
        gnum = int(input("Guess the number!: "))
        if gnum > rnum:
            print("That's too high.\n",warning.format(count))
        elif gnum < rnum:
            print("That's too low\n",warning.format(count))
        elif gnum > 99 or gnum < 0:
            print("That's out of range! Pick a number between 0 and 99")
        else:
            print("{}!".format(choice(praise)))
            break
    
#fun_guess(5)









