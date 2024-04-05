from turtle import Turtle, Screen

timmy = Turtle()
#
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
#     if _ % 2 == 0:
#         timmy.penup()
#     else:
#         timmy.pendown()

for _ in range(4):
    for i in range(10):
        if i % 2 == 0:
            timmy.penup()
            timmy.forward(10)
        else:
            timmy.pendown()
            timmy.forward(10)
    timmy.left(90)





screen = Screen()
screen.exitonclick()

