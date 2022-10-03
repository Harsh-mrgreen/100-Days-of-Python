X_CORD = [(0,0) , (-10, 0), (-20, 0)]  # CONSTANTS ARE ALWAYS ALL CAPS
MOVE_SEG = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
from turtle import Turtle, Screen

class Snake:

   def __init__(self) -> None:
       self.all_seg = []
       self.create_snake()
       self.head = self.all_seg[0]
    
    
   def create_snake(self):
       for position in X_CORD:
           self.add_seg(position)
           

   def add_seg(self, position):
       tim = Turtle("square")
       tim.color("white")
       tim.penup()
       tim.shapesize(0.8,0.8)
       tim.goto(position)
       self.all_seg.append(tim)

   def reset(self):
       for seg in self.all_seg:
           seg.goto(1000,1000)
       self.all_seg.clear()
       self.create_snake()
       self.head = self.all_seg[0]

    
   def extend(self):
       self.add_seg(self.all_seg[-1].position())



   def move(self):
        for seg in range(len(self.all_seg)-1, 0, -1):
            seg_x = self.all_seg[seg -1].xcor()
            seg_y = self.all_seg[seg -1].ycor()
            self.all_seg[seg].goto(seg_x,seg_y)

        self.head.forward(MOVE_SEG)


   def up(self):
       if self.head.heading() != DOWN:
           self.head.setheading(UP)

   def down(self):
       if self.head.heading() != UP:
           self.head.setheading(DOWN)

   def right(self):
       if self.head.heading() != LEFT:
           self.head.setheading(RIGHT)
   def left(self):
       if self.head.heading() != RIGHT:
           self.head.setheading(LEFT)

