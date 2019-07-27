import turtle
import random 

t = turtle.Pen()
t.width(10)

for x in range(6):
    t.setheading(-60*x)
    for x in range(6):
        a = random.randint(0,1)
        b = random.randint(0,1)
        c = random.randint(0,1)
        t.color(a,b,c)
        t.forward(50)
        t.left(60)
    t.forward(50)
