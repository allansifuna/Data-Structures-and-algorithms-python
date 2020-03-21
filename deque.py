# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:34:15 2020

@author: allan sifuna,https://github.com/allansifuna
"""
class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.item==[]
    def add_rear(self,item):
        return self.items.insert(0,item)
    def add_front(self,item):
        return self.items.append(item)
    def remove_front(self):
        return self.items.pop()
    def remove_rear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

