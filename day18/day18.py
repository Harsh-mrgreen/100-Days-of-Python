#from turtle import Turtle, Screen
import random
import turtle as t
t.colormode(255)


timmy = t.Turtle()
timmy.shape("turtle")
#timmy.color("Blue")

# for move in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for move in range(25):
#     timmy.color("Black")
#     timmy.forward(10)
#     timmy.color("White")
#     timmy.forward(10)

# for move in range(25):
#     for colors in ["Black" , "White"]:
#         timmy.color(colors)
#         timmy.forward(10)
# for move in range(25):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["Blue", "Green", 'Black', "Red", "Blue", "Green", 'Black', "Red"]
# for sides in range(3,11):
#     color = colors[sides - 3]
#     timmy.color(color)
#     angle = 360 / sides
#     for side in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r,g,b


# directions = [0,90,180,270]
# #colors = ["Blue", "Green", 'Black', "Red", "Blue", "Green", 'Black', "Red"]
# timmy.width(5)
# timmy.speed("fastest")
# for i in range(500):
#     timmy.color(random_color())
#     timmy.forward(20)
#     timmy.setheading(random.choice(directions))

def spyrograph(count):
    timmy.speed(0)
    #count = 60
    for i in range(count): 
        timmy.color(random_color())       
        timmy.circle(100) 
        timmy.left(360/count)

spyrograph(60)    



    

screen = t.Screen()
screen.exitonclick()