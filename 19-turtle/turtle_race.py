from turtle import Turtle, Screen
import random as r
screen = Screen()
screen.setup(width=500, height=400, startx=0, starty=0)

is_race_on = False

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
user_bet = screen.textinput(title="Place your bet", prompt=f"What color will win {colors}")
startpoint = -125.0
start = -230.0
turtles = []
for i in range(len(colors)):
    the_turtle = Turtle(shape="turtle")
    the_turtle.penup()
    the_turtle.color(colors[i])
    the_turtle.goto(start, startpoint)
    startpoint += 50.0
    turtles.append(the_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for i in turtles:
        go = r.randint(0, 10)
        i.forward(go)
        if i.xcor() >= 230:
            is_race_on = False
            if i.pencolor() == user_bet:
                print(f"Your bet was correct. {i.pencolor()} won!")
            else:
                print(f"You bet wrong. {i.pencolor()} won!")
            break

screen.listen()
screen.exitonclick()
