# For extracting the color from the image using colorgram
# rgb_values = []
#
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_values.append(rgb)
#
# print(rgb_values)
import random
import turtle
from turtle import Turtle, Screen
import random as r
tim = Turtle()
screen = Screen()


rgb_values = [(239, 241, 246), (233, 244, 239), (245, 235, 242), (242, 239, 228), (22, 30, 46), (140, 173, 200), (36, 105, 148), (205, 160, 112), (226, 210, 99), (140, 29, 62), (169, 51, 83), (208, 74, 101), (192, 139, 172), (16, 163, 191), (64, 167, 115), (136, 88, 73), (117, 181, 115), (190, 182, 43), (223, 81, 47), (27, 61, 117), (172, 209, 179), (72, 34, 67), (51, 141, 110), (9, 90, 108), (239, 204, 5), (217, 176, 195), (115, 36, 34), (232, 169, 162), (146, 208, 226), (186, 186, 212)]
tim.hideturtle()
turtle.colormode(255)
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.pendown()
tim.setheading(0)

for row in range(10):
    for column in range(10):
        tim.dot(20, r.choice(rgb_values))
        tim.penup()
        tim.forward(30)
        tim.pendown()
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(300)
    tim.setheading(0)
    tim.pendown()


screen.exitonclick()