# import module turtle
from turtle import Turtle, Screen

logo = """
 ______     ______   ______     __  __           ______           ______     __  __     ______     ______   ______     __  __    
/\  ___\   /\__  _\ /\  ___\   /\ \_\ \         /\  __ \         /\  ___\   /\ \/ /    /\  ___\   /\__  _\ /\  ___\   /\ \_\ \   
\ \  __\   \/_/\ \/ \ \ \____  \ \  __ \        \ \  __ \        \ \___  \  \ \  _"-.  \ \  __\   \/_/\ \/ \ \ \____  \ \  __ \  
 \ \_____\    \ \_\  \ \_____\  \ \_\ \_\        \ \_\ \_\        \/\_____\  \ \_\ \_\  \ \_____\    \ \_\  \ \_____\  \ \_\ \_\ 
  \/_____/     \/_/   \/_____/   \/_/\/_/         \/_/\/_/         \/_____/   \/_/\/_/   \/_____/     \/_/   \/_____/   \/_/\/_/ 
                                                                                                                                 
"""

# Intro Game with instructions
print(logo)
print("Welcome to Etch-a-Sketch !")
print("Use the arrows to sketch.")
print("Press 'c' to clear the screen and start drawing again.")
print("Press 'space' or click over the screen to end the game.")
input("Press 'enter' to start.")

# starts GUI and sketch pen
sketch_pen = Turtle() 
screen = Screen()

# draws forwards
def move_forwards():
    sketch_pen.forward(10)

# draws backwards
def move_backwards():
    sketch_pen.backward(10)

# points pen to left
def turn_left():
    new_heading = s.heading() + 10
    sketch_pen.setheading(new_heading)

# points pen to the right
def turn_right():
    new_heading = s.heading() - 10
    sketch_pen.setheading(new_heading)

# clears GUI and centers sketch pen again     
def clear():
    s.clear()
    s.penup()
    s.home()
    s.pendown()

# exits Game
def exit_game():
    screen.bye()

# adds eventListener to screen
screen.listen()
# connects "Up" key to move_forwards function
screen.onkey(move_forwards, "Up")
# connects "Down" key to move_backwards function
screen.onkey(move_backwards, "Down")
# connects "Left" key to turn_left function
screen.onkey(turn_left, "Left")
# connects "right" key to turn_right function
screen.onkey(turn_right, "Right")
# connects "c" key to clear function
screen.onkey(clear, "c")
# exits game on "space" key
screen.onkey(exit_game, "space")

