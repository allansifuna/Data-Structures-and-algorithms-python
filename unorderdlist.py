# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
from node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        return True

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def pop(self):
        previous = None
        current = self.head
        while current != None:
            if current.get_next() == None:
                if previous != None:
                    previous.set_next(None)
                else:
                    self.head = None
            previous = current
            current = current.get_next()

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                raise ValueError("Item not in UnorderedList")
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def get_first(self):
        current = self.head

        while current != None:
            if current.next == None:
                return current.get_data()
            else:
                current = current.get_next()

    def check(self):
        return self.reverse()

    def reverse(self, k):
        current = self.head
        previous = None
        while current != None:
            while current != None and k > 1:
                print(k)
                k -= 1
                next = current.next
                current.next = previous
                previous = current
                current = next

        self.head = previous
        return self

    def removeDuplicate(self):
        if self.head == None:
            return self.head
        current = self.head.get_next()
        previous = self.head
        inList = {}
        while current != None:
            if previous.get_data() not in inList:
                inList[previous.get_data()] = True
            if current.get_data() in inList:
                previous.set_next(current.get_next())
                current = current.get_next()
                continue
            previous = current
            current = current.get_next()
        return self

    def __str__(self):
        current = self.head
        s = []
        while current != None:
            s.insert(0, str(current.get_data()))
            current = current.get_next()
        return "->".join(s)
