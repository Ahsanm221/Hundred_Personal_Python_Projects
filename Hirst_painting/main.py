import colorgram
# rgb_colors = []
# colors = colorgram.extract('spots.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import Turtle, Screen
import turtle
import random

color_list = [(240, 231, 71), (180, 21, 47), (223, 241, 247), (115, 179, 203), (189, 77, 41),
              (27, 122, 165), (204, 155, 101), (21, 139, 90), (210, 73, 110), (176, 46, 65),
              (192, 175, 26), (21, 164, 208), (27, 40, 73), (211, 133, 153), (81, 171, 99),
              (38, 44, 108), (207, 75, 57)]

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.hideturtle()
tim.forward(350)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
