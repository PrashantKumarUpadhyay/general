import math
import os
import random
import re
import sys

x=int(input("Enter the Number:"))

def check(x):
    while True:
        try:        
            if x < 1 or x > 100:
                raise ValueError
            break
        except ValueError:
            print("The number entered is not between 1 and 100")
        break
def condition(x):
    if (x%2!=0):
        print("Weird")
    elif (x%2==0) and (1<x<6) or (x>20):
        print("Not Weird")
    elif (x%2==0) and (5<x<20) and (x<100):
        print("Weird")        
check(x)
condition(x)