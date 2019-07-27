# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#create a integer variable
myvar = 3
#create a string variable
mystring = "moon"
myString = "hyun"
#concatenate string variable using +
print(mystring+myString)
##put str(myvar) can solve problem
print(mystring+str(myvar))
#print(myvar + mystring)
#THIS WILL CAUSE AN ERROR!!
print("--------------------------------------------------------")
myage = 22
myname = "jung"
mygpa = 4.9
#this concarenates a string and an integer variable
print("My age is %d"%myage)
#this concarenates a string and a string variable
print("My name is %s" %myname)
#this concarenates a string and a float variable
print("My gpa is %f" %mygpa)
##put str(myvar) can solve problem
print(mystring+str(myvar))
print("--------------------------------------------------------") 
#list = group of variables

###create a favorite band on the list
###print second item
###print the number of item in the list
###add one item to the end of the list
###print out the number of items in the list
###print out the entire list 

#len() how long
#list.append
print("--------------------------------------------------------")
bigbang = ["top","g dragon","sun","victory","daesong"]
print(bigbang[1])
print("there are %d" % len(bigbang),"items in the list")
bigbang.append("milk")
print("there are %d" % len(bigbang))
print(bigbang)
print(bigbang[0])
print(bigbang[1])
print(bigbang[2])
print(bigbang[3])
print(bigbang[4])
print("--------------------------------------------------------") 
mylist = ["soda","fitz","hite"]
omg = mylist + bigbang
print(omg)
print(len(omg))
print("--------------------------------------------------------") 
#loop
#use a for loop to print out all the names
## x is a other variable that doesnt have specific datatype
mylist = ["soda","fitz","hite"]
for x in mylist:
    print(x)
print("--------------------------------------------------------")      
for x in range(3):
     print(mylist[x])     
print("--------------------------------------------------------")        
for o in omg:
    print(o)    
print("--------------------------------------------------------")    
for x in range(11):
    print(x)
print("--------------------------------------------------------")    
for x in range(3):
    print(mylist[1])
print("there are %d" % len(mylist),"items in the list")
print("--------------------------------------------------------") 
thenum = []
for x in range(13):
     thenum.append(x)
print(thenum)
print("--------------------------------------------------------") 
the = []

for x in range(13):
     the.append(x)
     print(the)   
print("--------------------------------------------------------")    
