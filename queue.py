# -*- coding: utf-8 -*-
"""
Created on Sat March 21 11:40:46 2020

@author: allan sifuna,https://github.com/allansifuna
"""
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        return self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

