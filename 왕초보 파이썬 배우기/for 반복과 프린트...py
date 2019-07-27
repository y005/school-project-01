# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#we define a fuction
def printmyname():
    #don't forget to indent
    print("my name is berry")

#let's call the fuction
printmyname()

#we can call the function in a loop
for x in range(5):
    printmyname()

#passing variables
#declare a string variable
thename = "Bob"

#define the function
def printanyname(thename):
    print("my name is %s" %(thename))

printanyname(thename) 

#use function in a loop
#create a list
allthefood = ["apple","banana","steak","pizza"]
#define the function
def printthecurrentfood(thefood):
    print("the current food is %s" %(thefood))
#call the fuction i a loop
#create a loop using the lengenth of the array as the range
for x in range(len(allthefood)):
    #call the fuction
    printthecurrentfood(allthefood[x]) 
    
   

    










