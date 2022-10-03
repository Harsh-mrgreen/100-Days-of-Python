from time import time
from turtle import Turtle, Screen

from zmq import PROTOCOL_ERROR_ZMTP_MALFORMED_COMMAND_MESSAGE
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 600 , height = 600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.05)
    
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_position()
        score.total_score()
        snake.extend()

    # detect collision with the boundary
    if snake.head.xcor()  > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    
    # detect collision with its tail
    for seg in snake.all_seg[2:]:
        # if seg == snake.head:
        #     pass

        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

        


    
   
    
        
        
        


screen.exitonclick()
