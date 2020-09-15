import math
import os
import random
import re
import sys
from array import array

#dir1=C//Users/upadh/Desktop/check1
#dir2=C//Users/upadh/Desktop/check2
list1=[]

var1="C:\\Users\\upadh\\Desktop\\check1"
#print(var1)
var2="C:\\Users\\upadh\\Desktop\\check2"
#print(var2)



# w=os.getcwd()
# print(w)
# os.chdir('C:\\Users\\upadh\\Desktop\\check1')
def checkingfiles(var1,var2):
    val={}
    list1=[]
    list2=[]
    x=os.listdir(var1)
    y=os.listdir(var2)
    for i in x:
        if i in y:
            list1.append(i)
            fs1=os.path.getsize(str(var1)+"\\"+i)
            fs2=os.path.getsize(str(var2)+"\\"+i)
            if fs1==fs2:
                list2.append(i)
    val["list1"]=list1
    val["list2"]=list2
    return val

# listz=[]
# listsz=[]

# def absolutepath(var):
#     for root, dirs, files in os.walk(os.path.abspath(var)):
#         for file in files:
#             z=os.path.join(root,file)
#             listz.append(z)
#     print(listz)        

# # def checkingSize(listz):
# #     for files in listz:
# #         size=os.path.getsize(files)
# #         print(size)

# absolutepath(var1)
# absolutepath(var2)  
# checkingfiles(x,y,list1)
#checkingSize(listz)
#absolutepath(var1)
print(checkingfiles(var1,var2))