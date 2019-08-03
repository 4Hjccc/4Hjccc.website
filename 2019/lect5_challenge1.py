# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:39:36 2019

@author: work
"""

import random
num = random.randint(1, 15)
cnt=1
correct = False

while((not correct) and cnt<=4 ):
    guess = input("Enter your number (1-15): ")
    
    if guess.isdigit():
        guess_num = int(guess)
        if (guess_num>num):
            print("Your guess is too large")
        elif (guess_num<num):
            print("Your guess is too small")
        else:
            print("Your guess is correct!")
            correct = True
        cnt = cnt+1
    else:
        print("Please enter an integer number")

if (correct):
    print("You win the game")
else:
    print("You lose the game. The number is", num)