import math
import os
import random
import re
import sys

n=int(input("Enter the number:"))

def fizzbuzz(n):
    val=""
    if n%3==0 and n%5!=0:
        #print(str(n) +":fizz")
        return "fizz"
    elif n%5==0 and n%3!=0:
        #print(str(n) + ":buzz")
        return "buzz"
    elif n%3==0 and n%5==0 and n!=0:
        #print(str(n) +":fizzbuzz")
        return "fizzbuzz"
    return val

d={}
for i in range(0,n):
    x=fizzbuzz(i)
    if x: 
        d[i]=x
print(d)
