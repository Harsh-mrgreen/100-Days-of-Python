STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle
from scoreboard import Scoreboard



class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        self.forward(MOVE_DISTANCE)

    def levelup(self):
        # if self.ycor() >= FINISH_LINE_Y:
        #     score.levelup()
        self.goto(STARTING_POSITION)
    
