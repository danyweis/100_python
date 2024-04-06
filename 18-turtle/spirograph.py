import turtle as t
# from 18-turtle import Turtle, Screen
import random

t.colormode(255)
timmy = t.Turtle()
radius = 150
total_circles = 5


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    the_color = (r, g, b)
    return the_color


def calc_angle(t_circles):
    calculated_angle = 360 / t_circles
    return calculated_angle


timmy.speed(0)
angle = calc_angle(total_circles)
current_heading = 0
for _ in range(0, total_circles):

    tup = random_color()
    timmy.pencolor(tup)
    timmy.circle(radius)
    timmy.setheading(timmy.heading() + angle)








screen = t.Screen()
screen.exitonclick()
