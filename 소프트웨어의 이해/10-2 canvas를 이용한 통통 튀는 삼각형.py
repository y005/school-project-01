from tkinter import *
import random
import time

x = 10
y = 15

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
canvas.create_polygon(250, 400, 275, 450, 225, 450)
                             
while True:
    canvas.move(1, x, y)
    position = canvas.coords(1)
   #tk.update()
    #time.sleep(0.05)

    if position[1] < 0:
        y = -y    
    if position[2] > 500:
        x = -x
    if position[3] > 500:
        y = -y
    if position[4] < 0:
        x = -x
       
    tk.update()
    time.sleep(0.05)
