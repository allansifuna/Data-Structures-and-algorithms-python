# class Stack:
#     """Stack using Lists"""
#     def __init__(self):
#         self.items=[]
#     def is_empty(self):
#         return len(self.items)==0
#     def peek(self):
#         return self.items[0]
#     def push(self,item):
#         return self.items.insert(0,item)
#     def pop(self):
#         return self.items.pop(0)
#     def search(self,item):
#         return item in self.items
#     def reverse(self):
#         self.items=self.items[::-1]
#         return self
#     def size(self):
#         return len(self.items)
#     def __str__(self):
#         return "->".join(list(map(str,self.items)))

#================================
#Stack Using Unordered LinkedList
#================================

# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
from unorderdlist import UnorderedList
class Stack:
    """Stack Using linkedList"""
    def __init__(self):
        self.items=UnorderedList()
    def is_empty(self):
        return self.items.is_empty()
    def peek(self):
        a=self.items.get_first()
        return a
    def push(self,item):
        return self.items.add(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return self.items.size()
    def check(self):
        return self.items.check()
    def reverse(self):
        return self.items
    def __str__(self):
        return str(self.items.reverse())
