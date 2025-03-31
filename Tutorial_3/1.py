import turtle

def starshape(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
turtle.speed(3)
starshape(100)
turtle.done()