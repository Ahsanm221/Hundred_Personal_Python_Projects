import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
timmy = Turtle()


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tup = (r, g, b)
    return color_tup


directions = []
for i in range(360):
    directions.append(i)

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(rand_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(10)


screen = Screen()
screen.exitonclick()
