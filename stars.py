import math
import os
import random
import re
import sys

n=int(input("Enter the value of n:"))
for i in range(0,n):
    line=""
    #adding front spaces to the line
    line=" "*(n-i)
    for j in range(0,i):
        line=line + "* "
    print(line)