# -*- coding: utf-8 -*-
"""
Created on Wed March 18 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""


from stack import Stack
from queue import Queue
from deque import Deque
from node import Node
from unorderdlist import UnorderedList
from orderedlist import OrderedList
from binarytree import BinaryTree

stack=Stack()
queue=Queue()
deque=Deque()
lst=UnorderedList()
olst=OrderedList()

#===============
#Testing a Stack
#===============

def populate(stack,string):
    """Add the string to the stack"""
    for i in string:
        stack.push(i)
def reverse(stack):
    """With LIFO the last character to be added
        to the stack will be the first to be read"""
    new_string=" "
    while not stack.is_empty():
        new_string+=stack.peek()
        stack.pop()
    return new_string

# string="To Be Reversed"
# populate(stack,string)
# print(reverse(stack))


def Deci2Bin(n):
    """Populate the stack with remainders of the operation"""
    while n>0:
        stack.push(divmod(n,2)[1])
        n//=2

def readDeci2Bin(stack):
    """Read the stack"""
    s=""
    while not stack.is_empty():
        s+=str(stack.peek())
        stack.pop()

    return s

Deci2Bin(100)
# print(stack.pop())
print(stack)

print(readDeci2Bin(stack))


#===============
#Testing a Queue
#===============

def hot_potato(lst,num):
    for i in lst:
        queue.enqueue(i)

    return queue

#===============
#Testing a Deque
#===============
def populate_deque(deque,string):
    for i in string:
        deque.add_front(i)
    return deque
def check_palindrome(queue):
    while queue.size()>1:
        if queue.remove_rear()!=queue.remove_front():
            return False
    return True
# dq=populate_deque(deque,"allanalla")
# print(check_palindrome(dq))

#============
#Testing Node
#============
a=Node(10)
b=Node(12)
a.set_next(b)

# print(a.get_next())

#=====================
#Testing Unorderedlist
#=====================
lst.add(20)
lst.add(23)
lst.add(120)
lst.add(8)
lst.add(198)
# print(lst.reverse())
# print()
# print(lst.reverse())
# print(lst.size())

#=====================
#Testing Orderedlist
#=====================
olst.add(20)
olst.add(23)
olst.add(120)
olst.add(8)
olst.add(198)
# v=olst
# print(olst.size())
# print(v.reverse())
# print(olst)

#====================
#Testing A BinaryTree
#====================

r=BinaryTree(10)
r.insert_left_child(12)
r.insert_right_child(15)
r.get_left_child_val().insert_left_child('b')
# print(r.get_left_child_val().get_left_child_val().get_root_val())

def binarySearch(l,item):
    low,high=0,len(l)-1
    while low<=high:
        mid=(low+high)//2
        # print(f"low:{low},{mid},high:{high}")
        guess=l[mid]
        if guess==item:
            return mid
        if guess>item:
            high=mid-1
        else:
            low=mid+1
    return None

# a=[i for i in range(10**2)]
# print(binarySearch(a,11))

# def binSearch(l,item):
#     low,high=0,len(l)-1

#     while low<=high:
#         mid=(low+high)//2
#         guess=l[mid]
#         if guess==item:
#             return mid
#         if guess>item:
#             high=mid-1
#         else:
#             low=mid+1
#     return None
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        # print(f"Arr:{arr}")
        # print(f"New Arr:{newArr}")
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
from time import perf_counter
def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        left=[i for i in arr[1:] if i<=pivot]
        right=[i for i in arr[1:] if i>pivot]
        return quickSort(left)+[pivot]+quickSort(right)

from random import shuffle

# a=[i for i in range(10000)]
# b=[i for i in range(10000)]
# shuffle(a)
# shuffle(b)
# v1=perf_counter()
# selectionSort(a)
# v2=perf_counter()
# print(f"Selection Sort:{v2-v1}s")

# v3=perf_counter()
# quickSort(b)
# v4=perf_counter()
# print(f"quickSort Sort:{v4-v3}s")
