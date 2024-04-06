import colorgram as c
import random
import turtle as t

t.colormode(255)
timmy = t.Turtle()
number_of_dots_per_row = 10
colors = c.extract('bart.jpg', 10)
color_palet = []
dot_thickness = 15

for color in colors:
    rgb = color.rgb
    color_palet.append(rgb)


def random_color(c_palet):
    the_color = random.choice(c_palet)
    r = the_color.r
    g = the_color.g
    b = the_color.b
    dot_color = (r, g, b)
    return dot_color


row_position = -250.0
for dot in range(0, number_of_dots_per_row):
    timmy.goto(-250.0, row_position)
    row_position += 30
    for row in range(0, number_of_dots_per_row):
        # timmy.pencolor()
        timmy.pendown()
        timmy.dot(dot_thickness, random_color(color_palet))
        timmy.penup()
        timmy.forward(30)
# timmy.home()

screen = t.Screen()
screen.exitonclick()