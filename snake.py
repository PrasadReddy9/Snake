from turtle import Turtle


STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            tur = Turtle("square")
            tur.color("white")
            tur.penup()
            tur.goto(position)
            self.segment.append(tur)

    def move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
            self.segment[0].forward(20)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def Down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def Left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def Right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
