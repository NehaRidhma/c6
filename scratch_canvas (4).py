import turtle

side = int(input(' enter sides'))
length = int(input('enter length'))
def draw_polygon():
    for variable in range(0, side):
        turtle.forward(length)
        turtle.right(360 / side)

draw_polygon()
turtle.penup()
turtle.goto(80, 100)
turtle.pendown()

draw_polygon()