import turtle

def hexdesign(size):
    for _ in range(6):
        turtle.forward(size)
        turtle.right(60)

def radial_pattern(n, count):
    for _ in range(count):
        hexdesign(n)
        turtle.right(360 / count)

turtle.speed(0.5)
radial_pattern(50, 10)

turtle.done()