import turtle
pen=turtle.Turtle()
scr=turtle.Screen()
scr.bgcolor('black')
pen.pencolor('white')
pen.speed(0)


v=100
for i in range(v):
    pen.forward(i*5)
    #in clock wish direction
    pen.right(145)
    pen.hideturtle()


turtle.done()