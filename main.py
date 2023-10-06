import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

    # another way to get coordinates of mouse click
    # def get_mouse_click_coor(x,y):
    #     print(x, y)
    #
    # turtle.onscreenclick(get_mouse_click_coor)
    #

data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()

# loop = True
# correct= []
guessed_states = [] # not mine
# while loop:
while len(guessed_states) < 50:
    #     prompt_text = f"Total: {len(correct)} \n What's another state name?"
    #     answer_state = screen.textinput(title="Guess the State", prompt=prompt_text)

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state name?")

    # 1 convert to title case
    answer_state = answer_state.title()
    #
            #     def move(x,y):
            #         turtle.penup()
            #         turtle.setpos(x, y)
            #         turtle.write(state)
            #         turtle.setpos(0,0)
            #         turtle.pendown()
    #
    # 2 check if is 50 states

    if answer_state == "Exit":

        states_to_learn = [state for state in all_states if state not in guessed_states]

        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn', index=False)

        break


    if answer_state in all_states:
        t = turtle.Turtle()     # not mine
        t.hideturtle()          # not mine
        t.penup()               # not mine

        state_data = data[data.state == answer_state]
            # state_data_list = (choice.values.tolist())[0]
            # state = choice_list[0]
            # x, y = choice_list[1], choice_list[2]
            # move(x,y)
        t.goto(int(state_data.x), int(state_data.y))  # not mine
        t.write(answer_state)           # not mine
            # correct.append(state)
        guessed_states.append(answer_state)
    #     else:
    #         print("not in states")
    #         loop = False
    #
    #

#turtle.mainloop() # keep screen open after click

# states_to_learn.csv




