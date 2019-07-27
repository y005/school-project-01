from tkinter import *
import time


tk = Tk()
canvas = Canvas(tk, width = 800, height = 800)
canvas.pack()
scores = []
i = 0

print('5개의 점수를 입력하세요.')
for x in range(5):
    score = int(input('점수 입력: '))
    scores.append(score)

for x in scores:

     if x >= 90:
        x1 = 100
        y1 = 100 + i
        x2 = 100 + x*3
        y2 = 100 + 50 + i
        canvas.create_rectangle(x1,y1,x2,y2,fill =  'green')
        canvas.create_text(x2+40 ,y1+20 , text = str(x))

     elif x >= 80 and x < 90:
        x1 = 100
        y1 = 100 + i
        x2 = 100 + x*3
        y2 = 100 + 50 + i
        canvas.create_rectangle(x1,y1,x2,y2,fill =  'blue')
        canvas.create_text(x2+40 ,y1+20 , text = str(x))

     elif x >= 60 and x < 80:
        x1 = 100
        y1 = 100 + i
        x2 = 100 + x*3
        y2 = 100 + 50 + i
        canvas.create_rectangle(x1,y1,x2,y2,fill =  'orange')
        canvas.create_text(x2+40 ,y1+20 , text = str(x))

     else:
        x1 = 100
        y1 = 100 + i
        x2 = 100 + x*3
        y2 = 100 + 50 + i
        canvas.create_rectangle(x1,y1,x2,y2,fill =  'red')
        canvas.create_text(x2+40 ,y1+20 , text = str(x))

     i += 100

     tk.update()
     time.sleep(0.5)
