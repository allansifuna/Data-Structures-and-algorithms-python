# -*- coding: utf-8 -*-
"""
Created on Sat March 14 21:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
from random import choice
a="""Choose one of the following topics and construct a formal essay
 that is either predominantly narrative or descriptive in nature. At
  some level, you may be mixing the two, but your essay  should either
  seek to tell a ​narrative story or creates a ​descriptive​ dominant impression.
  In either case, you should create an essay with a thesis, either explicit or
   implied, that adheres to the conventions of the mode you choose"""
names=a.split()
name=choice(names)
life=len(name)
guess=''
while life>0:
    s=[i if i in guess else '_' for i in name]
    print("".join(s))
    print(f"life:{life}")
    a=input("Guess a letter\n")
    if a in name:
        if a not in guess:
            print("You guessed right")
            guess=guess+a
    else:
        life-=1
    if len(guess)==len(set(name)):
        break
if life==0:
    print('You were hanged')
else:
    print(f'You guessed "{name}" right')

