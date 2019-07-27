# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 14:38:06 2018

@author: SM-PC
"""
#1
#print statement
print("hello bob, that's a nice shirt")
#print a number
print(120)
#print number and a string
print("23")
#print an integer = number
#using "" make number string
#print a float - a float has a decimal place
print(2.33)
#2
#variables are container that have value
mynumber = 22
myname = "moon"
myfloat = 6.11
#we can assign variable simultaneously
myvar1, myvar2 = 22, 24
firstname, lastname = "bob","robert"

#print variable
print(mynumber)
#we can add 2 variable stall the result in a 3rd
thesum = mynumber + myvar1
#we can print variables
print(mynumber)
print(myname)
print(myfloat)
print(thesum)
#we can print many variable using a coma
print(myvar1,myvar2,firstname,lastname)
#we can concatenate strings using + sign
print(firstname + lastname)

#we can add strings,integers and floats with a + sign 
#NOTE we have to typecast the integer and the float as strings
print(str(mynumber)+myname+str(myfloat))
#we can concatenate variable and text
print("i love th number %d" % mynumber)
print("my favorite beatle is %s" % myname)
print("i am %f" % myfloat + "percent sure")
#use %g for general format to remove the 0's
print("i am %g" % myfloat + "percent sure")
#or 
#use %. number of decimal places>f 
print("i am %.3f" % myfloat + "percent sure")

#we can place several variables in the print statement
print("i am %g percent sure and %s is %d" %(myfloat,myname,mynumber))

#we can build the string before printing 
data = (myfloat,myname,mynumber)
print("i am %g percent sure and %s is %d" %data)

#lists
mynumlist = [12,18,16,99]
mystrlist = ['coffee','pizza','chicken','pasta']
myfloatlist = [1.2,4.6,7.33,67.3]

#we can also create empty list
mynewlist =[]
#we can add to the list
mynewlist.append("items0")
mynewlist.append("items1")
mynewlist.append("items2")
mynewlist.append("items3")
#we can also see the content of list
print(mynumlist)
print(mystrlist)
print(myfloatlist)
print(mynewlist)
#we can see the value of specific item by calling its location
print(mynumlist[0])
print(mystrlist[1])
print(myfloatlist[2])
print(mynewlist[3])

#we can add list together 
combinelist = mynumlist + myfloatlist 
print(combinelist)

#we can also the lengenth of a list using len() command
strlistlength = len(mystrlist)
numlistlength = len(mynumlist)
floatlistlength = len(myfloatlist)
newlistlength = len(mynewlist)

print(strlistlength)
print(numlistlength)
print(floatlistlength) 
print(newlistlength)
#for loops
#we us for loop to move through data
for x in mystrlist:
    print(x)
#the variable x is our choice - we can use any name
for d in mynumlist:
    print(d)
#we can set a range to count in
for x in range(10):
    print(x)   
    
for x in range(3):
    print(myfloatlist[x])           

#conditionals and operators
#create a variable
x = 5
#operators 
#>(greater than), <(less than),==(equal),<=(less than or equal),>=(greater than or equal),!=(not equal)

#use two = (equal signs) to compare
print(x == 10)#return false
print(x == 5)#return true

# < less than > grater than
print(x < 10)#return true
print(x > 10)#return false

#less than or equal <=,greater than or equal >=
print(x <= 5)#return true
print(x >= 30)#return false

#not equal !=
print(x != "cheese cake")#return true
print(x != 5 )#return false

#conditionals
#if  statement
if x == 5:
    print("x DOES equal 5")

#if else statement
if x == 15:
    print("x DOES equal!")
else:
    print("x DOES NOT equal!")

#create two new variables
#compare two variables
x = 32
y = 50    

if x == y:
    print("x and y are same")
else:
    print("x and y are different")


if x <= y:
    print("x is less than or equal to y")
else:
    print("x is greater than y")    
if x >= y:
    print("x is greater than or equal to y")
else:
    print("x is less than y")    


if x != y:
    print("%d DOES not equal %d"%(x,y))
else:
    print("%d DOES equal %d"%(x,y))
    
#evaluate several outcomes
#create a variable
myvar = 200

if myvar == 5:
    print("5 is the value ")    
elif myvar == 10:
    print("5 is the value ")    
elif myvar == 15:
    print("5 is the value ")    
elif myvar == 20:
    print("5 is the value ")    
else:
    print("no values match")    

#input
#create variable that contain the result of user input 
#variablename = value return from function    
name = input("what is your name? :D")
#datatype of input value is always string   
print("nice to meet you~ " + name + " ouo")
age = input("your age?: ")
print("So " + name + ", you are already " + age + " year old :D")
print("you don't look a day over 19. How do you look so good")

#user input
name = input("what is your name?")
favoritefood = input("what is your favorite food?")    
print("Nice to meet you " + name +", i like "+ favoritefood + " too!")

#random numbers
#import the random library
from random import randint

#create a variable to hold the random number
#variablename = randint(low,high)
myrandom = randint(1,6)
myother = randint(1,6)

print("you roll a %d and a %d!" %(myrandom,myother))

























































