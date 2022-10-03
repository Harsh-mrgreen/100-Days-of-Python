from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle you think is going to win? ").lower()
colors = ["Blue", "Green", 'orange', "Red", 'yellow', 'purple']
all_turtles = []

for index in range(len(colors)):

    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230,-125 + (50 * index))
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on == True:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You have won! {winning_color} is the winner")
            
            else:
                print(f"You have lost! {winning_color} is the winner")
        else:
            random_move = random.randint(0,10)
            turtle.forward(random_move)
        
    

screen.exitonclick()
