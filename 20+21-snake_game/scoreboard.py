from turtle import Turtle

TEXT_CORD = 270
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        # self.speed("fastest")
        self.penup()
        self.goto(0, TEXT_CORD)
        self.hideturtle()
        # self.reprint()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()




