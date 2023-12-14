import turtle
abhi=turtle.Turtle()
scr=turtle.Screen()

abhi.speed(0)
scr.bgcolor('black')
abhi.pencolor('cyan')

abhi.penup()
abhi.goto(0, 100)
abhi.pendown()

c=0
d=0
while True:
    for i in range(4):
        abhi.forward(80)
        abhi.right(90)
    abhi.right(15)
    c+=1
    if c>=390/15:
         abhi.forward(50)
         c=0
         d+=1
         if d>12:
             break

# for i in range(4):
        #abhi.forward(80)
        #abhi.right(90)
    #abhi.right(5)
    #c+=1
    #if c>=360:
    # break 


turtle.done()