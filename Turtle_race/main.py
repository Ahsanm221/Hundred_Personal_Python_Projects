import turtle
import random
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle is going to win? Enter their color: ")

colors = ["red", "orange", "coral", "green", "blue", "purple"]
y_shift = -70
is_race_on = False
all_turtles = []

for turtle_index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    y_shift += 30
    new_turtle.goto(x=-230, y=y_shift)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've Won! The {winner_color} turtle is the winner!")
            else:
                print(f"You lost! The {winner_color} turtle won! ")
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)


screen.exitonclick()