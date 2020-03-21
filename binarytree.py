# -*- coding: utf-8 -*-
"""
Created on Sat March 21 12:03:56 2020

@author: allan sifuna,https://github.com/allansifuna
"""
class BinaryTree:
    def __init__(self,root):
        self.key=root
        self.left_child=None
        self.right_child=None
    def insert_left_child(self,new_node):
        if self.left_child==None:
            self.left_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.left_child=self.left_child
            self.left_child=t
    def insert_right_child(self,new_node):
        if self.right_child==None:
            self.right_child=BinaryTree(new_node)
        else:
            t=BinaryTree(new_node)
            t.right_child=self.right_child
            self.right_child=t

    def get_right_child_val(self):
        return self.right_child

    def get_left_child_val(self):
        return self.left_child

    def get_root_val(self):
        return self.key
    def set_roor_val(self,obj):
        self.key=obj
        return True
    @staticmethod
    def preorder(tree):
        if tree:
            print(tree.get_root_val())
            BinaryTree.preorder(tree.get_left_child_val())
            BinaryTree.preorder(tree.get_right_child_val())
    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
