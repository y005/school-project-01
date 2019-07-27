# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:52:24 2018

@author: SM-PC
"""
#conditional
#create a variable
x = 5
#use 2 = signs for comparing
print(x == 10)
#ㄴfalse
print(x == 5)
#ㄴtrue
print("--------------------------------------------------------")
#operator ==,>=,<=,<,>,!=
#less than greater than
print(x < 10)
print(x > 10)
print("--------------------------------------------------------")
#less or equal,greater or equal
print(x <= 5)
print(x >= 30)
print("--------------------------------------------------------")
#!= not equal
print(x != 10)
x = "hello"
print(x != "hello")
x = 5 
print(x != 5)
print("--------------------------------------------------------")
#if statment
if x == 5:
    print("X DOES EQUAL five!")
if x == 10:
    print("X DOES EQUAL five!")    
#else statment
else:
    print("X DOES NOT EQUAL FIVE!")
print("--------------------------------------------------------")    
#create a variable 
y = 10
if x == y:
    print("x and y are the same")
else:
    print("x and y are different")    
print("--------------------------------------------------------")
x = 32
y = 10
if x == y:
    print("x and y are the same")
else:
    print("x and y are different")       
print("--------------------------------------------------------")
x = 32
y = 32
if x == y:
    print("x and y are the same")
else:
    print("x and y are different")     
print("--------------------------------------------------------")
x = 32
y = 10
if x <= y:
    print("x is small or equal than y")
else:
    print("x is greater than y")     
print("--------------------------------------------------------")
x = 12
y = 100
if x >= y:
    print("x is greater or equal than y")
else:
    print("x is smaller than y")     
print("--------------------------------------------------------")
if x != y:
    print("%d does not equal %d" %(x,y))
else:
    print("%d does equal %d"%(x,y))  
print("--------------------------------------------------------")    