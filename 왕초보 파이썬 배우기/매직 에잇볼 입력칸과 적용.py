# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 14:22:20 2018

@author: SM-PC
"""

#import the tkinter module
#NOTE DO NOT DO THIS -> IMPORT tkinter *
import tkinter as tk

#import fuctionality for creating random numbers
from random import randint

#begin building gui(graphic user interface)
#create the window
#create a tkinter object and give it a name
window = tk.Tk()

#give the window a title 
window.title('My First Window')

#set the size of the window in pixels
#objectname.geometry('width x height')
window.geometry('720x486')

def begin():
    #create the new text
    newtext = 'What is your name?'

    #place the new text in the label
    lbl.configure(text = newtext)
    #create new button for the button and the function call
    newbuttontext = 'enter'
    btn.configure(text = newbuttontext,command = greetme)

def greetme():
    #create new text
    newtext = 'hello ' + txt.get() + ' I sense a mystery in your heart!'
    
    #place a new text in the label
    lbl.configure(text = newtext)
    
    newbuttontext = 'True'
    btn.configure(text = newbuttontext,command = askquestion)
    
    #remove the text from the input field
    txt.delete(first = 0, last =35)
    
def askquestion():
    #create new text
    newtext = 'What is your question?'
    
    #place a new text in the label
    lbl.configure(text = newtext)
    
    newbuttontext = 'ASK'
    btn.configure(text = newbuttontext,command = getfortune)

def getfortune():
    #create the new text
    newtext = 'AH '+txt.get()+ ' is a good question'

    #place the new text in the label
    lbl.configure(text = newtext)
    #create new button for the button and the function call
    newbuttontext = 'Yes'
    btn.configure(text = newbuttontext,command = fortuneresult)  
    
    #remove the text from the input field
    txt.delete(first = 0, last =35)

def fortuneresult():
    #generate random num
    myrandom = randint(0,3)
    
    if myrandom == 0:
        answer = "Yes, definately! do you need more question?"
    elif myrandom == 1:
        answer = "No way~~~~! Go suck a lemon! do you need more question?"
    elif myrandom == 2:
        answer = "Ask me later. the sprits are busy. do you need more question?"
    lbl.configure(text = answer)    
    
    newbuttontext = 'Yes'
    
    btn.configure(text = newbuttontext,command = askquestion)
   
    txt.delete(first = 0, last = 35)
     
#crete a label
lbl = tk.Label(window,text = 
               'Are you ready to know the future?'
               ,font = ('Ariel Bold', 12),wraplength = 300)

#put the label in the label
lbl.pack()

#creat a text entry field
txt = tk.Entry(window, width = 35)

#set the text box to be ready for input
txt.focus()

#put the text entry field in the window
txt.pack()


#create a Button
btn = tk.Button(window, text = 'yes!',command = begin)

#put the button in the window
btn.pack()

#run the tkinter app
window.mainloop()
