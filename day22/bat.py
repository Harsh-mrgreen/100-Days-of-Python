from turtle import Turtle , Screen

class Bat(Turtle):

    def __init__(self, Position) -> None:
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid =5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(Position)
    



    def moveup(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
      

    def movedown(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
       
