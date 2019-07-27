# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 14:03:17 2018

@author: SM-PC
"""

#frame example

#import tkinter library
import tkinter as tk

#add extra tkinter library
from tkinter import TOP
from tkinter import BOTTOM

#begin building gui (graphic user interface)
#create the window
window = tk.Tk()

#give the window a title
window.title('my tk template')

#set the size of the window in pixels
window.geometry('350x500')

#this is WHERE your function go




#add element to the window
#create the frames
topframe = tk.Frame(window)
topframe.pack(side = TOP)

bottomframe = tk.Frame(window)
bottomframe.pack(side = BOTTOM)

#add labels
#create label to the TOP frame
toplabel = tk.Label(topframe, text = "top label")

#create label to the BOTTOM frame
bottomlabel = tk.Label(bottomframe, text = "bottom label")


#add button
#create button for the top frame 
topbutton = tk.Button(topframe, text = "top button")

#create button for the button frame
bottombutton = tk.Button(bottomframe, text = "buttom button")

#add text fields
toptextfield = tk.Entry(topframe)
bottomtextfield = tk.Entry(bottomframe)

#load the image the image should be in the same file folder
image1 = tk.PhotoImage(file = "8-ball.png")
image2 = tk.PhotoImage(file = '8-ball.png')

#add images 
#topimage = tk.Label(topframe, image = image1)
#bottomimage = tk.Label(bottomframe,image = image2)

#add label to hold the images
topimagelabel = tk.Label(topframe,image = image1)
bottomimagelabel = tk.Label(bottomframe,image = image2)

#pack all the elements
toplabel.pack()
bottomlabel.pack()

topbutton.pack()
bottombutton.pack()

toptextfield.pack()
bottomtextfield.pack()

topimagelabel.pack()
bottomimagelabel.pack()

#run the loop
window.mainloop()



