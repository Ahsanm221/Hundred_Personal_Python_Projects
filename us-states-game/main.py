import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
guessed_states = []
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = [state for state in list_of_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in list_of_states:
        state_info = data.loc[data.state == answer_state]
        writer.goto(state_info.iloc[0, 1], state_info.iloc[0, 2])
        writer.write(answer_state)
        guessed_states.append(answer_state)
    else:
        print("That isn't a state. Guess again")

    # state_info = data[data.state == answer_state]
    # writer.goto(int(state_info.x), int(state_info.y))
