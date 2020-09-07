import math
import os
import random
import re
import sys

x=input("Please enter the string:")
y=x.lower()
#print(type(x))
def numvwl(y):
    a=y.count("a")
    #print(type(a))
    b=y.count("e")
    c=y.count("i")
    d=y.count("o")
    e=y.count("u")
    ans=a+b+c+d+e
    print("The answer is:",ans)
numvwl(y)