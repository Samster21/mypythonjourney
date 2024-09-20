# import turtle, pandas
#
# my_screen = turtle.Screen()
#
#
# joe = turtle.Turtle()
# joe.penup()
# joe.hideturtle()
# turtle.bgpic(picname="blank_states_img.gif")
#
#
# count = 0
#
# df = pandas.read_csv("50_states.csv")
#
# states = df["state"]
#
# while count < 50:
#     answer = my_screen.textinput(title="Guess the State!", prompt="Try guessing a state!")
#     answer = answer.title()
#     if answer in states:
#         row = df[df.state == answer ]
#         xcor = row.x.item()
#         ycor = row.y.item()
#         joe.goto(xcor, ycor)
#         joe.write(arg=f"{answer}")
#         count+=1

import turtle, pandas

my_screen = turtle.Screen()

joe = turtle.Turtle()
joe.penup()
joe.hideturtle()
turtle.bgpic(picname="blank_states_img.gif")


df = pandas.read_csv("50_states.csv")

states = df["state"].tolist()  # Convert states to a list for easy comparison

guessed_states = []

while len(guessed_states) < 50:
    answer = my_screen.textinput(title=f"{len(guessed_states)}/50 correct!", prompt="Try guessing a state!")
    answer = answer.title()
    if answer == "Exit":
        missing = []
        for state in states:
            if state not in guessed_states:
                missing.append(state)
        new_states = pandas.DataFrame(data=missing)
        new_states.to_csv("states_to_learn.csv")
        break
    if answer in states and answer not in guessed_states:
        row = df[df.state == answer]
        joe.goto(row.x.item(), row.y.item())
        joe.write(arg=f"{answer}")
        guessed_states.append(answer)
