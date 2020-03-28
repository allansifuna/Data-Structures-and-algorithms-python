# -*- coding: utf-8 -*-
"""
Created on Sat March 21 11:21:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
from node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def add(self, item):
        current = self.head
        stop = False
        previous = None

        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
        return temp

    def index(self, item):
        if not self.search(item):
            return -1
        else:
            current = self.head
            count = 0

            while current.get_data() != item:
                count += 1
                current = current.get_next()
            return count

    def reverse(self):
        current = self.head
        prev = None

        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        return self

    def removeDuplicate(self):
        if self.head == None:
            return self.head
        current = self.head.get_next()
        previous = self.head
        inList = []
        while current != None:
            if previous.get_data() not in inList:
                inList.append(previous.get_data())
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
