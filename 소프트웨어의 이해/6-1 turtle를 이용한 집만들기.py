import turtle

t = turtle.Pen()
#창문 2개

t.up()
t.goto(-150,100)
t.down()

#setheading 함수는 포인트에서 절대적인 각으로 상대적인 움직임이 아니
for x in range(4):
    t.setheading(90-90*x)
    for x in range(4):
        t.forward(50)
        t.right(90)

t.up()
t.goto(200,100)
t.down()
for x in range(4):
    t.setheading(90)
    t.right(90*x)
    for x in range(4):
        t.forward(50)
        t.right(90)
#문짝
t.up()
t.goto(-10,30)
t.down()
t.setheading(0)

for x in range(2):
    t.forward(100)
    t.right(90)
    t.forward(130)
    t.right(90)

#집 형체

t.up()
t.goto(-300,300)
t.down()

for x in range(2):
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)    

#지붕
t.setheading(60)
t.forward(600)
t.right(120)
t.forward(600)
