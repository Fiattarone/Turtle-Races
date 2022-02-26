import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
screenothy = Screen()
screenothy.setup(width=500, height=400)
turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for x in range(6):
    turtles.append(Turtle(shape="turtle"))
    turtles[x].penup()
    turtles[x].color(colors[x])
    turtles[x].goto(x=-225, y=(x-3)*30)

user_bet = screenothy.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

racing = False
winning_color = ""

if user_bet:
    racing = True

while racing:
    for x in turtles:
        x.forward(random.randint(0, 10))
        if x.xcor() > 230:
            winning_color = x.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print("Boo you lost.")
            racing = False

screenothy.exitonclick()
