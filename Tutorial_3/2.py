import turtle
def pentagonshape(n):
    for _ in range(5):
        turtle.forward(n)
        turtle.left(72)
turtle.speed(1)
pentagonshape(100)
turtle.done()