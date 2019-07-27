# 시계의 테두리가 포함된 프로그램
 
from tkinter import *
import time
import math

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.configure(background='white')
canvas.pack()

width = 500
height = 500
cx = width/2        # center x
cy = height/2       # center y

sr = height/2-50    # radius for second hand
mr = height/2-80	# radius for minute hand
hr = height/2-110	# radius for hour hand

while 1:
    t = time.localtime()    
    hour = (t[3] + t[4]/60)* 30
    minute = (t[4] + t[5]/60)*6
    second = t[5]*6

    canvas.delete("all")
    # clock outline
    canvas.create_arc(10,10,width-10,height-10, extent=359,style=CHORD, width = 2)    
    hx = hr * math.sin(hour/360 * 3.14*2)
    hy = hr * math.cos(hour/360 * 3.14*2)

    #parameter
    for x in range(60):

        아1 = 240 * math.sin(6*x/360 * 3.14*2)
        아2 = 240 * math.cos(6*x/360 * 3.14*2)
        어1 = 아1 * 0.9
        어2 = 아2 * 0.9
        if x % 5 == 0:
            canvas.create_line(cx+아1, cy-아2, cx+어1, cy-어2, fill='Black', width = 8)   
        canvas.create_line(cx+아1, cy-아2, cx+어1, cy-어2, fill='Black', width = 5)   

    #요일 표시
    요일 =['월','화','수','목','금','토','일']   
    요일표시 = str(t[1]) +'월 '+ str(t[2])+'일('+요일[t[6]]+')'
    canvas.create_text(250, 400, text = 요일표시, font = ('Arial',10), fill ='Purple')
    canvas.create_rectangle(210, 370, 290, 430, outline = 'Purple')


    #오후,오전 표시
    if t[3] < 12:
        canvas.create_text(250, 100, text = "AM", font = ('Arial',10))
    else: 
        canvas.create_text(250, 100, text = 'PM', font = ('Arial',10))
    canvas.create_rectangle(220, 75, 280, 125, outline = 'Orange')    
    
    # hour hand
    canvas.create_line(cx, cy, cx+hx, cy-hy, fill='Blue', width = 10)   
    mx = mr * math.sin(minute/360 * 3.14*2)
    my = mr * math.cos(minute/360 * 3.14*2)

    # minute hand 
    canvas.create_line(cx, cy, cx+mx, cy-my, fill='Green', width = 6)    
    sx = sr * math.sin(second/360 * 3.14*2)
    sy = sr * math.cos(second/360 * 3.14*2)

    # second hand
    canvas.create_line(cx, cy, cx+sx, cy-sy, fill='Red', width = 2)

    # center circle
    canvas.create_arc(cx-10, cy-10, cx+10, cy+10, extent=359,style=CHORD, width = 2, fill = 'black')
    
    time.sleep(0.1)
    tk.update()
