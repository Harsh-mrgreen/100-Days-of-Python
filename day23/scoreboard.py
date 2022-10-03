from turtle import Turtle


FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.levelup()
    
    def levelup(self):
        self.clear()
        self.write(f"level: {self.level}",False, font = FONT)
        self.level += 1

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over")
