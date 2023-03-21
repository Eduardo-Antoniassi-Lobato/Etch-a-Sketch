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



