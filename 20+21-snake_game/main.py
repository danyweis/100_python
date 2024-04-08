from turtle import Screen, Turtle, Shape

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE Game")

game_on = True
snake = Turtle("square")
snake.penup()
snake.color("white")
snake.speed("slowest")
# snake.width(20)
# snake.pensize(20)
head_position = (0.0, 0.0)
head_direction = "e"
snakes = []
body_x = [0.0, -10.0, -20.0]
body_y = [0.0, 0.0, 0.0]

for i in range(body_x):
    snake = Turtle("square")
    snake.penup()
    snake.color("white")
    snake.speed("slowest")
    snakes.append(snake)

while game_on:
    for i in range(len(snakes)):

        if head_direction == "e":
            body_x.insert(0, )

        position = (body_x[i], body_y[1])
        snakes[i].goto(position)






screen.exitonclick()
