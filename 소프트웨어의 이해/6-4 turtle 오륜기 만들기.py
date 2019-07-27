#터틀을 여러개 소환하며
#for를 이용하여 여러개의 터틀이 한번에 그리기
#원그리기 나눠서 엣지 길이 

import turtle

turtle.setup(width = 1000, height = 500)
edges = 30
length = 400/edges
angle = 360/edges

t1 = turtle.Pen()
t2 = turtle.Pen()
t3 = turtle.Pen()
t4 = turtle.Pen()
t5 = turtle.Pen()

t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)

t1.width(5)
t2.width(5)
t3.width(5)
t4.width(5)
t5.width(5)

t1.up()
t2.up()
t3.up()
t4.up()
t5.up()

t1.setposition(-200,100)
t2.setposition(-100,100)
t3.setposition(0,100)
t4.setposition(-150,0)
t5.setposition(-50,0)

t1.down()
t2.down()
t3.down()
t4.down()
t5.down()

t1.pencolor('blue')
t2.pencolor('black')
t3.pencolor('red')
t4.pencolor('yellow')
t5.pencolor('green')

for x in range(edges):
    
    t1.forward(length)
    t1.right(angle)

    
    t2.forward(length)
    t2.right(angle)

    
    t3.forward(length)
    t3.right(angle)

    
    t4.forward(length)
    t4.right(angle)

    
    t5.forward(length)
    t5.right(angle)


