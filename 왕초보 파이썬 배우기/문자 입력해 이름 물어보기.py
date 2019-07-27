# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 13:20:36 2018

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
    newtext = 'Hi '+ txt.get()+' You Are Better Than I Imagine'

    #place the new text in the label
    lbl.configure(text = newtext)
    
#crete a label
lbl = tk.Label(window,text = 
               'Hello What Is Your Name?'
               ,font = ('Ariel Bold', 12),wraplength = 300)

#put the label in the label
lbl.pack()

#creat a text entry field
txt = tk.Entry(window, width = 40)

#set the text box to be ready for input
txt.focus()

#put the text entry field in the window
txt.pack()


#create a Button
btn = tk.Button(window, text = 'click me!',command = begin)

#put the button in the window
btn.pack()

#run the tkinter app
window.mainloop()













