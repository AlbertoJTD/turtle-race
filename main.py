from turtle import Turtle, Screen
import random

screen = Screen()

# Set up the screen
screen.setup(width=700, height=500)
user_bet = None

# Sep up turtle characteristics
colors = ['red', 'blue', 'purple', 'green', 'orange', 'black', 'brown']
turtle_list = []
y_position = [-150, -100, -50, 0, 50, 100, 150]
is_race_on = False

# Ask the user's bet
while True:
    user_bet = screen.textinput(title='Make your bet',
                                prompt='Which turtle will win the race? Select a color(red, blue, purple, green, orange, black, brown) >:').lower()
    if user_bet in colors:
        break

# Create the turtles
for x in range(7):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[x])
    turtle.penup()
    turtle.goto(x=-320, y=y_position[x])

    turtle_list.append(turtle)

# Race starting
is_race_on = True
winner = None
while is_race_on:
    for turtle in turtle_list:
        random_steps = random.randint(0, 10)
        turtle.forward(random_steps)

        if turtle.xcor() >= 330:
            winner = turtle
            is_race_on = False
            break

# Check if the user's bet is correct
if user_bet == winner.pencolor():
    print(f'You have won! The {winner.pencolor()} turtle is the winner!')
else:
    print(f'You have lost! The {winner.pencolor()} turtle won!')


screen.exitonclick()
