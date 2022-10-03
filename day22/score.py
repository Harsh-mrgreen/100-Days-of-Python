from turtle import Turtle

class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,280)
        

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", 12)
    
    def score_board(self):
        self.clear()
        self.write(f"score :- {self.player1_score} : {self.player2_score}", False, "center", 12)
       
