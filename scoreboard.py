from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.score = 0
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.write(f"Score : {self.score}",align="center", font=("Courier", 24, "normal"))

    def game(self):
        self.goto(0, 0)
        self.write( "Game Over", align="center", font=("Courier", 20, "normal"))

    def increase(self):
        self.score = +1
        self.clear()
        self.score_board()


