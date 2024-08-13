import turtle

def segmentLine(x1, y1, x2, y2, color = "black", size = 1):
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(10 if size > 10 else size)
    turtle.goto(x2,y2)
    turtle.penup()
    turtle.hideturtle()
    turtle.done()
segmentLine(0,0,100,100)
segmentLine(500,500,200,200)
