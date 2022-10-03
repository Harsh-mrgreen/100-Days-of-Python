from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.highscore = int(data.read())
        self.color("red")
        self.penup()
        self.setposition(0,280)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score :  {self.score}, Highscore : {self.highscore}", False, "center", 12)

    def total_score(self):
        self.score += 1
        self.update_scoreboard()
        
    
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
            
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", False, "center", 12)

