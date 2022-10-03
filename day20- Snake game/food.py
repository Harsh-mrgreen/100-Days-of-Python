from turtle import Turtle
import random
#from xxlimited import foo


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed(0)
        self.new_position()
        
    
    def new_position(self):
        x_cord = random.randint(-270, 270)
        y_cord = random.randint(-270, 270)
        self.goto(x_cord, y_cord)





        
        