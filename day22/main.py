from turtle import Turtle, Screen
from bat import Bat
from ball import Ball
import time
from score import Score
screen = Screen()
screen.setup(width= 800, height = 600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)


#bat = Bat()
r_bat = Bat((350,0))
l_bat = Bat((-350,0))

ball = Ball()
score = Score()
screen.update()
screen.listen()

screen.onkey(r_bat.moveup, "Up")
screen.onkey(r_bat.movedown, "Down")
screen.onkey(l_bat.moveup, "w")
screen.onkey(l_bat.movedown, "s")

game_is_on = True
while game_is_on:
    score.score_board()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if  ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()
    
    if (ball.distance(r_bat) < 50 and ball.xcor() > 330) or (ball.distance(l_bat) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        
        

    if ball.xcor() > 360:
        ball.reset_position()
        score.player1_score += 1
        
        
        
    elif ball.xcor() < -360:
        #score.game_over()
        ball.reset_position()
        score.player2_score += 1
        
        
        
    

    











screen.exitonclick()
