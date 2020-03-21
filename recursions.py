# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
def sum_of_lists(n):
    if len(n)==1:
        return n[0]
    else:
        return n[0]+sum_of_lists(n[1:])

a=[3,5,6,7,4,5,4,3,2]
# print(sum_of_lists(a))

# import turtle
# my_turtle = turtle.Turtle()
# my_win = turtle.Screen()
# def draw_spiral(my_turtle, line_len):
#     if lineLen > 0:
#         my_turtle.forward(line_len)
#         my_turtle.right(90)
#         draw_spiral(my_turtle, line_len - 5)
# draw_spiral(my_turtle, 100)
# my_win.exitonclick()


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)
def move_disk(fp,tp):
    print("moving disk from",fp,"to",tp)
move_tower(2, "A", "B", "C")
