from turtle import Turtle, Screen
import random

timmy = Turtle()
sides = 3
max_sides = 10
running = True
length = 100


def random_color():
    r = random.randint(0, 100) / 100
    g = random.randint(0, 100) / 100
    b = random.randint(0, 100) / 100
    return r, g, b


while running:
    angle = 360 / sides
    # r = random.randint(0,100)/100
    # g = random.randint(0,100)/100
    # b = random.randint(0,100)/100
    # tup = (r, g, b)
    tup = random_color()
    timmy.width(5)

    timmy.pencolor(tup)
    for i in range(sides):
        timmy.forward(length)
        timmy.right(angle)
    sides += 1
    if sides > max_sides:
        running = False

screen = Screen()
screen.exitonclick()

