import colorgram
import random
import turtle as t
t.colormode(255)
# colors = colorgram.extract('image.jpg', 2**1000)
# color_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb1.b
#     new_color = (r,g,b)
#     color_rgb.append(new_color)

# print(color_rgb)

color_list = [(247, 242, 234), (237, 242, 248), (249, 240, 244), (239, 247, 244), (139, 168, 195), (206, 154, 121), (192, 140, 150), (25, 36, 55), (58, 105, 140), (145, 178, 162), (151, 68, 58), (137, 68, 76), (229, 212, 107), (47, 36, 41), (145, 29, 36), (28, 53, 47), (55, 108, 89), (228, 167, 173), (189, 99, 107), (139, 33, 28), (194, 92, 79), (49, 40, 36), (228, 173, 166), (20, 92, 69), (177, 189, 212), (29, 62, 107), (113, 123, 155), (172, 202, 190), (51, 149, 193), (166, 200, 213), (66, 66, 57), (107, 140, 129), (47, 69, 76), (178, 124, 75)]

timmy = t.Turtle()
def hirst():
    for row in range(10):
        timmy.setpos(0,50 * row)
        for i in range(10):
            timmy.color(random.choice(color_list))
            timmy.dot(20)
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        timmy.penup()

hirst()
    
        




screen = t.Screen()
screen.exitonclick()