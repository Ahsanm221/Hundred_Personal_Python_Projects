from turtle import Turtle
SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(to_angle=90)
        self.setposition(x=0, y=-280)

    def move(self):
        self.forward(SPEED)

    def reset_position(self):
        self.setposition(x=0, y=-280)
