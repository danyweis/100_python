from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backwards():
    timmy.backward(10)


def turn_counter_clockwise():
    timmy.left(10)


def turn_clockwise():
    timmy.right(10)


def clear_the_screen():
    timmy.penup()
    timmy.clear()
    timmy.speed("fastest")
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_the_screen)





screen.exitonclick()