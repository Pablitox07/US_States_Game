import turtle
import pandas
from tkinter import messagebox
from turtle import Turtle, Screen
screen = turtle.Screen()
screen.title("U.S")
image = ("states.gif")
screen.addshape(image)
turtle.Screen()
screen.bgpic(image)
turtle.shape(image)


states = pandas.read_csv("50_states.csv")
states_dict = states.to_dict()

already_used=[]
tries = 0
game_on = True
while game_on:
    correct = False
    answer_state = screen.textinput(title="Guess", prompt="Guess state:").capitalize()
    for each_state in range(len(states_dict["state"])):
        if answer_state == states_dict["state"][each_state]:
            state_number = each_state
            if answer_state not in already_used:
                already_used.append(answer_state)
                state_turtle = turtle
                state_turtle.hideturtle()
                state_turtle.penup()
                state_turtle.goto(states_dict['x'][state_number], states_dict['y'][state_number])
                state_turtle.write(f"{answer_state}", align='center')
                correct = True
            elif answer_state in already_used:
                messagebox.showinfo("showinfo", "Already Used!!!")
                correct = True
    if not correct:
        tries += 1
        messagebox.showinfo("showinfo", f"Opportunities: {tries} of 3")
    if tries == 3:
        game_on = False

screen.mainloop()
