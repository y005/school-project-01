import turtle

t = turtle.Pen()

t.color('red')

t.begin_fill()

t.pencolor('black')
t.setheading(45)
t.circle(100, 180)
t.right(90)
t.circle(100,180)
t.forward(200)
t.left(90)
t.forward(200)

t.end_fill()
