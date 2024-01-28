import turtle
import pandas
import pyarrow
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

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50 US states", prompt="What's another state's name?").capitalize()
    if answer_state in states_list:
        print("Nice")
        score += 1
        mapper.state_on_map(answer_state)

    if score == 50:
        print("Well done! You've named all of the US states!")
        game_is_on = False

#def get_mouse_click_coor(x, y):
#    print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()
screen.exitonclick()
