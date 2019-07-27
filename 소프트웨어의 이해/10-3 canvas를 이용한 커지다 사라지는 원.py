
from tkinter import *
import random
import time

tk = Tk()

canvas = Canvas(tk, width = 300, height = 300 )
canvas.pack()

width = 300
height = 300

colors = ['blue','green','orange','red','yellow']

step = 5

while True:
 for i in range(0,151,10):

    canvas.delete('all')

    x1 = width/2 -i
    y1 = height/2 -i
    x2 = width/2 +i
    y2 = height/2 +i

    canvas.create_arc(x1,y1,x2,y2,extent = 359 , style = ARC, outline = random.choice(colors))
    tk.update()
    time.sleep(0.05)

 for i in range(151,-1,-10):

    canvas.delete('all')

    x1 = width/2 -i
    y1 = height/2 -i
    x2 = width/2 +i
    y2 = height/2 +i

    canvas.create_arc(x1,y1,x2,y2,extent = 359 , style = ARC, outline = random.choice(colors))
    tk.update()
    time.sleep(0.05)
        
        
