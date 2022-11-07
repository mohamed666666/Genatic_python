# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:23:34 2020

@author: Ahmed Omar
"""

#import numpy as np
import copy
class TreeNode:
    def __init__(self,s=None):
        self.strategy=s
        self.children=[]
        self.parent=None
        self.payoff=None
        self.count=0
    

    def add_child(self,child):
        p=self.parent
        if p:
            for c in range(len(p.children)):
                if c==0:
                    p.children[c].append_1_child(child)
                else:
                    p.children[c].append_1_child(copy.deepcopy(child))
        else:
            self.append_1_child(child)
    
#child.parent=self
    def append_1_child(self,child):
        for i in range(len(self.strategy)):
            if i==0:
                self.children.append(child)
            else:
                self.children.append(copy.deepcopy(child))
        for i in self.children:
            i.parent=self
        return self





    
    def print_tree(self):
        if self.children:
            self.name="player"+str(self.get_level())
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + str(self.name)+" Strategy:"+str(self.strategy))
            if self.children:
                for child in self.children:
                    child.print_tree()
        else:
             print(self.get_level()*" "*3+"Pays:"+str(self.payoff))
        return self


    def get_level(self):
        level = 1
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def set_payoff(self,pay):
        self.payoff=pay
        return self

    def preorderTraversal(self, preorder_list):
        """Traverse a general tree in preorder. Entry point the invoking node.
        Each node traversed is appended to a list
        Parameters: preorder_list Type list: element Type Node()
        Return: list of nodes traversed in preorder"""
        # add node to list preorder_list
        preorder_list.append(self)
        # recursively call self for each of node node_children
        for i in self.children:
            i.preorderTraversal(preorder_list)
            # once all nodes have been visited return list of nodes in preorder
        return preorder_list

    def get_leafs(self):
        leafnodes=[]
        nodes=self.preorderTraversal([])
        for i in range(len(nodes)):
            if not nodes[i].children:
                leafnodes.append(nodes[i])
        return leafnodes


    def back_induction(self,i,j,c,p):
        finalpath=[]
        h=c-1
        if self.children[i].children[j].children[c].payoff[p] >= self.children[i].children[j].children[h].payoff[p]:
            s=self.children[i].children[j].strategy[c]
            finalpath.append(s)
            print("player 3 will choose strategy",s)
            print("player 2 knows player 3 will always play",s)
            if self.children[i].children[j].children[c].payoff[p-1] >=self.children[i].children[j].children[h].payoff[p-1]:
                s=self.children[i].strategy[j]
                finalpath.append(s)
                print("player 2 will choose strategy",s)
                print("player 1 knows player 3 will always play",s)
                if self.children[i].children[j].children[j].payoff[p-2] >=self.children[i].children[j].children[h].payoff[p-2]:
                    s=self.strategy[i]
                    finalpath.append(s)
                    print("player 1 will choose strategy",s)
                else:
                    s=self.strategy[i-1]
                    finalpath.append(s)
                    print("player 1 will choose strategy",s)
            else:
                s=self.children[i].strategy[j-1]
                finalpath.append(s)
                print("player 2 will choose strategy",s)
        else:
            s=self.children[i].children[j].strategy[h]
            finalpath.append(s)
            print("player 3 will choose strategy",s)
            print("player 2 knows player 3 will always play",s)
            if self.children[i].children[j].children[c].payoff[p-1] >=self.children[i].children[j].children[h].payoff[p-1]:
                s=self.children[0].strategy[0]
                finalpath.append(s)
                print("player 2 will choose strategy",s)
                print("player 1 knows player 2 will always play",s)
                if self.children[i].children[j].children[c].payoff[p-2] >=self.children[i].children[j].children[h].payoff[p-2]:
                    s=self.strategy[i]
                    finalpath.append(s)
                    print("player 1 will choose strategy",s)
                else:
                    s=self.strategy[i-1]
                    finalpath.append(s)
                    print("player 1 will choose strategy",s)
            else:
                s=self.children[i].strategy[j-1]
                finalpath.append(s)
                print("player 2 will choose strategy",s)
        if len(finalpath)==3:
            print("best strategies")
            print("game will be :",finalpath[::-1])
            print("*******************************")
        else:
            print("the subgame perfect equilibrium of the game ")
            print("strategies :",finalpath[::-1])
            print("*******************************")
        return finalpath

    def back_induction_dynmic(self):
        strategies=[]
        for i in range(len(self.children)):
            for j in range(len(self.children[i].children)):
                for c in range(len(self.children[i].children[j].children)):
                    strategies=self.back_induction(i,j,c,2)
    def add_pays(self):
        paynode=TreeNode()
        leafs=self.get_leafs()
        for i in range(len(leafs)):
            leafs[i].append_1_child(copy.deepcopy(paynode))
        return self


###########################################################
if __name__=="__main__":
    payoffs=[(1,2,5),(4,1,4),(2,1,3),(2,3,6),(3,3,6),(3,2,5),(4,2,4),(1,4,7)]
    print("######################################################################")
    test=TreeNode(s=[1,2])
    test2=TreeNode(s=[3,4])
    test.add_child(test2)
    test3=TreeNode(s=[5,6])
    test2.add_child(test3)
    test=test.add_pays()#works only for three players in the feature
    leafs=test.get_leafs()
    for i in range(len(leafs)):
        leafs[i].set_payoff(payoffs[i])
    print("TREE")
    test.print_tree()
    print("#####################################################################")
    print("Bckward Induction:")
#test.back_induction()
    test.back_induction_dynmic()
    