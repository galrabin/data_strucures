#!/usr/bin/env python3
from math import pow
class Node:
    def __init__(self,data=None,left=None,right=None,parent=None,height=0):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = height

    def print(self):
        print("(Data : {D}, Height : {H}".format(D=self.data,H=self.height),end="")
        if self.parent != None:
            print(", Parent : {P}".format(P=self.parent.data), end="")
        if self.left != None:
            print(", Left : {L}".format(L=self.left.data),end="")
        if self.right != None:
            print(", Right : {R}".format(R=self.right.data),end="")
        print(")")


class bst:
    def __init__(self):
        self.root = Node()

    def insert(self,data):
        current = self.root
        if self.root.data == None:
            self.root.data = data
        else:
            current = self.root
            for i in range(self.root.height+1):
                if current.data > data:
                    if current.left != None:
                        current = current.left
                    else:
                        new_node = Node(data,None,None,current)
                        current.left = new_node
                        break
                else:
                    if current.right != None:
                        current = current.right
                    else:
                        new_node = Node(data,None,None,current)
                        current.right = new_node
                        break
        while current.parent != None:
            current.parent.height += 1
            current = current.parent

    def find(self,value):
        current = self.root
        for i in range(self.root.height + 1):
            if current.data == value:
                return current
            elif current.data > value:
                if current.left == None:
                    return "under flow"
                current = current.left
            else:
                if current.right == None:
                    return "under flow"
                current = current.right

    def min_right_tree(self,current):
        if current.right != None:
            current = current.right
            while current.left != None:
                current = current.left
            return current

    def successor(self,value):
        current = self.find(value)
        current = self.min_right_tree(current)
        if current == None:
            while current.parent != None and current.left != None:
                parent = current.parent
                if parent.left == current:
                    return parent
                current = parent.parent
        if current == self.find(value):
            return "No successor"
        return current


    def remove(self,value):
        deleted = self.find(value)
        new_node = deleted
        while new_node.parent != None:
            new_node.parent.height -= 1
            new_node = new_node.parent
        if deleted.right == None and deleted.left == None:
            if deleted.parent.right == deleted:
                deleted.parent.right = None
                deleted = None
            else:
                deleted.parent.left = None
                deleted = None
        elif (deleted.right != None and deleted.left == None) or (deleted.right == None and deleted.left != None):
            if deleted.right != None:
                if deleted.parent.right == deleted:
                    deleted.parent.right = deleted.right
                    deleted.right.parent = deleted.parent
                    deleted = None
                else:
                    deleted.parent.left = deleted.left
                    deleted.left.parent = deleted.parent
                    deleted = None
        elif (deleted.right != None and deleted.left != None):
            min = self.min_right_tree(deleted)
            deleted.data = min.data
            if min.parent.right == min:
                min.parent.right = None
            else:
                min.parent.left = None
            min = None


    def print_bst(self, state, current = "empty"):
        if current == "empty":
            current = self.root
        if current != None:
            #LDR
            if state == "inorder":
                self.print_bst("inorder",current.left)
                print(current.data,end=" ")
                self.print_bst("inorder",current.right)
            #LRD
            if state == "postorder":
                self.print_bst("postorder", current.left)
                self.print_bst("postorder", current.right)
                print(current.data, end=" ")
            #DLR
            if state == "preorder":
                print(current.data ,end=" ")
                self.print_bst("preorder", current.left)
                self.print_bst("preorder", current.right)
