from turtle import Turtle

TEXT_CORD = 280

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(y=TEXT_CORD, x=0)
        self.hideturtle()
        self.score = 0
        self.reprint()

    def reprint(self):
        self.clear()
        self.goto(y=TEXT_CORD, x=0)

        self.write(arg=f"Score: {self.score}", move=True, align="center", font=('Arial', 10, 'normal'))



