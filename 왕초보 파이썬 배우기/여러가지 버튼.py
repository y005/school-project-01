# -*- coding: utf-8 -*-
"""
Created on Thu May 10 13:08:23 2018

@author: SM-PC
"""
#import the tkinter library
import tkinter as tk

#import ttk from tkinter
from tkinter import ttk

#from tkinter import the messagebox library
from tkinter import messagebox

#import the progress bar library from ttk
from tkinter.ttk import Progressbar

window = tk.Tk()

#create the window title
window.title('My UI elements')

#set the window size
window.geometry('800x300')

#add a label
label = tk.Label(window, text = '#1 Kpop Group is', font = ('Arial Bold',30 ))

#set the position and add the element to the window 
label.grid(column = 0, row = 0)

#create a combobox
combo = ttk.Combobox(window)

#set the content of the combobox items (list)
combo['values'] = ('Twice','Crayon Pop','Girls Generation','T-ara','Black Pink','Red Velvet')

#set the current selection 
combo.current(0)

#add the combobox to the window
combo.grid(column = 1, row = 0)

#create a checkbutton
chkbtn = ttk.Checkbutton(window, text = 'is this true?')

#add the checkbutton to the window
chkbtn.grid(column = 2, row = 0)

#add a radio button
radiobtn =ttk.Radiobutton(window, text ='Are you Sure?', value = 1)

#add a radio button to the window
radiobtn.grid(column = 0, row = 1)

#add a messagebox
def clicked():
    #messagebox.showinfo('Emergency Alert!!!' , 'You have a virus!!!')
    #messagebox.askquestion('You sneezed ', 'Do You Have a Cold?')
    #messagebox.askyesno('I Have a Question', 'Are Plates Food?')
    #messagebox.askyesnocancel('Save', 'Would You Like to Have a Dinner?')
    #messagebox.askoKcancel('Your Health', 'How is Your Health?')
    messagebox.askretrycancel('Save', 'I can not save this file.try again')
       
#create the button    
btn = tk.Button(window, text = 'click for prize' , command = clicked)   

#add the button to the window
btn.grid(column = 1, row = 1)

#create a spinbox object
spin = tk.Spinbox(window, from_ = 0, to = 10, width = 30)

#add the spinbox to the window
spin.grid(column = 2, row = 1)

#create the progressbar object
bar =Progressbar(window, length =100)

#set the bar value
bar['value'] = 75

#add the bar to the window
bar.grid(column = 0, row = 2)

window.mainloop()





