from turtle import Turtle
import pandas
states = pandas.read_csv("50_states.csv")
#arizona = states[states.state == "Arizona"]
#print(arizona.iloc[0]["x"])


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def state_on_map(self, state):
        chosen_state = states[states.state == state]
        self.goto(x=chosen_state.iloc[0]["x"], y=chosen_state.iloc[0]["y"])
        self.write(state)
