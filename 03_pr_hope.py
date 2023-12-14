import turtle
abhi=turtle.Turtle()
scr=turtle.Screen()

abhi.speed(0)
scr.bgcolor('black')
abhi.pencolor('cyan')

abhi.penup()
abhi.goto(-70,10)
abhi.pendown()

a=0
while True:

    for i in range(4): #can change for more designe
        abhi.forward(i*60)
        abhi.right(130)
    abhi.right(30)
    a+=1
    if a >=360/10:
        break
    abhi.hideturtle()


turtle.done()