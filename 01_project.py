
import turtle
abhi=turtle.Turtle()
scr=turtle.Screen()

abhi.speed(0)
scr.bgcolor('black')
abhi.pencolor('cyan')

sides=9

def shape(size, sides):
    for i in range(sides):
        abhi.forward(size)
        abhi.left(360/sides)

for i in range(100):
    shape(5*i, sides)
    abhi.left(i)

turtle.done()        
