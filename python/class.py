import random
import turtle

colors = ['#FAF0E6','#66CDAA','#000000','#191970','#EEEE00','#D02090','#8B4513','#8A2BE2','#228B22']
turtle.setup(600,600)
turtle.bgcolor("#8E8E8E")
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(10)
for i in range(36):
    pen.color(random.choice(colors))
    pen.begin_fill()
    pen.right(10)
    for i in range(3):
        pen.forward(240)
        pen.left(120)
    pen.end_fill()    
pen1 = turtle.Turtle()
pen1.hideturtle()
for i in range(10):
    pen1.color(random.choice(colors))
    pen1.right(36)
    pen1.begin_fill()
    for i in range(4):
        pen1.forward(100)#長度100
        pen1.left(90) 
    pen1.end_fill()  
turtle.done()
