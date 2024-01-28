import turtle
import pandas
from score import Writer

states = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
mapper = Writer()
score = 0

states_list = states.state.to_list()
guessed_states = []

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 US states",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        print(answer_state)
        score += 1
        mapper.state_on_map(answer_state)

    if score == 50:
        print("\nWell done! You've named all of the US states!")
        game_is_on = False

forgotten_states = [state for state in states_list if state not in guessed_states]
pandas.DataFrame(forgotten_states).to_csv("forgotten_states.cvs")
