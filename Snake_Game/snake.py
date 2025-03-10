from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.boxes = []
        self.create_snake()
        self.head = self.boxes[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_box(position)

    def add_box(self, position):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.boxes.append(snake)

    def extend(self):
        self.add_box(self.boxes[-1].position())

    def move(self):
        for box_num in range(len(self.boxes) - 1, 0, -1):
            new_x = self.boxes[box_num - 1].xcor()
            new_y = self.boxes[box_num - 1].ycor()
            self.boxes[box_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset(self):
        for box in self.boxes:
            box.goto(1000, 1000)
        self.boxes.clear()
        self.create_snake()
        self.head = self.boxes[0]
