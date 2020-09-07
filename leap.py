"""
import math
import os
import random
import re
import sys

x=int(input("Enter the year:"))
y=int(x%4)
if (y!=0):
    print("It is not a leap year")

def leap(x):
    if (x%4==0) and (x%400==0):
        print("it is a leap year")
    elif (x%4==0) and (x%100==0):
        print("It is not a leap year")
leap(x)
"""
import math
import os
import random
import re
import sys


def is_leap(year):
    leap = False
    while(year%4==0):
        if (year%400==0) and (year%100==0):
            leap = True
        break
    while (year%4==0):
        if (year%100!=0):
            leap = True
        break    
    return leap
year = int(input())
print(is_leap(year))