# -*- coding: utf-8 -*-
"""
Created on Fri March 20 22:37:56 2020

@author: allan sifuna,
"""
"""
    Created this game to help my brother and sister learn multiplication
    while at home after the closure of schools due to corona virus outbreak.
"""
from random import randint
i = input("What is Your Name: ")
z, *r = i.capitalize().split()
score = 0
quiz = 0
trials = True
while trials:
    s = randint(1, 9)
    j = randint(1, 9)
    wrong = True
    t = 2
    x = s * j
    quiz += 1
    while wrong:
        try:
            i = int(input(f"What is {s}*{j}="))
        except Exception:
            print("Enter a valid number")
        if i == -1:
            trials = False
            wrong = False
        elif i == x:
            print(f"Nice!! {z},  {s}*{j}={x}\n")
            score += 1
            wrong = False
        else:
            if t == 0:
                wrong = False
                print(f"Remember {z}, {s}*{j}={x}\n")
            else:
                t -= 1
                print(f"Wrong!! {z}, Try Again\n")

print(f"Nice Trial {z}, You got {score} out of {quiz-1}\n")
