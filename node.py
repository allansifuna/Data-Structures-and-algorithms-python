# -*- coding: utf-8 -*-
"""
Created on Sat March 21 09:03:30 2020

@author: allan sifuna,https://github.com/allansifuna
"""
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,new_data):
        self.data=new_data
        return self.data
    def set_next(self,new_next):
        self.next=new_next
        return self.next
    def __str__(self):
        return str(self.data)
