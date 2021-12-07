import turtle
import pandas
screen = turtle.Screen()
screen.setup(width=700,height=800)
screen.title("India Quiz Game")
image = "inde15.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("Book1.csv")
state = data.state.to_list()
guessed_state = []
while len(guessed_state)<29:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/29 State",prompt="What's another state name?").title()
    print(answer_state)
    if answer_state == "exit" or answer_state == "Exit":
        missing_state = []
        for states in state:
            if states not in  guessed_state:
                missing_state.append(guessed_state)
        print(missing_state)
        break
    if answer_state in state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)
turtle.mainloop()