#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 22:28:07 2020

@author: mohamed
"""

import numpy as np


def count_defctions(actions):
    c=0
    d=0
    for i in range(len(actions)):
        if actions[i]==0:
            c+=1
        else:
            d+=1
    return c>=d

A=np.array([[3,0],[5,1]])
B=np.array([[3,5],[0,1]])


strategies=["Per_DDC","Per_CCD","Tit For Tat","Hard Tit For Tat"
            ,"Soft Tit For Tat","Reverse Tit for Tat","Suspicious Tit For Tat",
            "Soft Majo","Hard Majo","Grim","Random"]
per_DDC=[1,1,0]
per_CCD=[0,0,1]

payoff1=0
payoff2=0

actions1=[]


print("========WELCOME TO IPD GAME========")

n=int(input("Enter Number Of rounds :"))
s=7
print("player choose '"+strategies[s]+"' aginst u : \n")
print("Game started plz choose between two actions '0=Cooperat' '1=defect'.")
counter=0
while n>0:
    
    a1=int(input("Enter action:"))
    actions1.append(a1)
    
    #per_DDC strategy
    if s==0:
        a2=per_DDC[counter]
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        if counter ==2:
            counter=0
        counter+=1
            
    #per_CCD strategy
    elif s==1:
        a2=per_CCD[counter]
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        if counter ==2:
            counter=0
        counter+=1
        
        
    # TIT for TAT strategy
    elif s==2:
        if counter==0:
            a2=0
        else:
            a2=actions1[counter-1]
            
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
        
     # HARD TIT for TAT strategy
    elif s==3:
        if counter==0:
            a2=0
        else:
            if actions1[counter-1]==1 and actions1[counter-2]==1:
                a2=1
            else:
                a2=0
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
    # soft TIT for TAT strategy
    elif s==4:
        if counter==0 or counter==1:
            a2=0
        else:
            if actions1[counter-1]==1 and actions1[counter-2]==1:
                a2=1
            else:
                a2=0
                
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
    
    #Reverse Tit for Tat strategy
    elif s==5:
        if counter==0:
            a2=1
        else:
            if a1==0:
                a2=1
            else:
                a2=0
            
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
        
    #Suspicious Tit For Tat strategy
    elif s==6:
        if counter==0:
            a2=1
        else:
            a2=actions1[counter-1]
            
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
        
    #Soft Majo strategy
    elif s==7:
        if counter==0:
            a2=0
        else:
            if count_defctions(actions1):
                a2=0
            else:
                a2=1
                
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
        
    #Hard Majo strategy 
    elif s==8:
        if counter==0:
            a2=0
        else:
            if not count_defctions(actions1):
                a2=1
            else:
                a2=0
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
        
    #Grim strategy
    elif s==9:
        if counter==0:
            a2=0
        else:
            if actions1[counter]==1:
                a2=1
            else:
                a2=0
        
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
    
    elif s==10:
        a2=np.random.randint(0,2)
        payoff1+=A[a1,a2]
        payoff2+=B[a1,a2]
        print("palyer choose to:",a2)
        print("your payoff "+str(payoff1))
        print("player payoff "+str(payoff2))
        counter+=1
 
    
    n-=1

