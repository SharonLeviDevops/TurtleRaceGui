from turtle import Turtle, Screen
import random

race_on = Turtle
def foward():
    rand = random.choice()
    new_turtle.forward(10)

new_turtle = Turtle()
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make you Bet ", "Which turtle will win? Enter your color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtles =[]


for turtle_i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_i])
    new_turtle.color(colors[turtle_i])
    all_turtles.append(new_turtle)

while race_on:
    for turtle in all_turtles:
        rand_dis = random.randint(0,10)
        turtle.forward(rand_dis)
        if turtle.xcor() > 230:
            win = turtle.pencolor()
            if win == user_bet:
                print("You win!!!!!")
            else:
                print("you loose!!!")


for turtle in all_turtles:
    rand_dis = random.r




screen.exitonclick()