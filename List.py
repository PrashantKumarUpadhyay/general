import math
import os
import random
import re
import sys

x=int(input("Enter the value of i:"))
y=int(input("Enter the value of j:"))
z=int(input("Enter the value of k:"))
n=int(input("Enter the value of n:"))
list1=[]

def prntarr(x,y,z):
    for i in range (0,x+1):
        for j in range (0,y+1):
            for k in range (0,z+1):
                if (i+j+k!=n):
                    list2=[i,j,k]
                    list1.append(list2)
    print(list1)                
prntarr(x,y,z)