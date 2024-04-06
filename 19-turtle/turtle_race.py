from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400, startx=0, starty=0)

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
user_bet = screen.textinput(title="Place your bet", prompt=f"What color will win {colors}")
startpoint = -125.0
for i in range(len(colors)):
    the_turtle = Turtle(shape="turtle")
    the_turtle.penup()
    the_turtle.color(colors[i])
    the_turtle.goto(-230.0, startpoint)
    startpoint += 50.0



screen.listen()

screen.exitonclick()