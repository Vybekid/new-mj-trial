import turtle
import time
import os

# 1. Set up the screen
screen = turtle.Screen()
screen.title("Animation")
screen.bgcolor("black")

# 2. Turn off automatic updates for manual control (KEY FIX for blank screen)
screen.tracer(0)

# 3. List and register the image files (must be GIFs)
image_files = ["6.gif", "7.gif", "8.gif", "9.gif"]
for image in image_files:
    # Check that the file actually exists before trying to use it
    if not os.path.exists(image):
        raise FileNotFoundError(f"Cannot find {image}. Make sure it's a GIF and in the same folder!")
    screen.addshape(image)

# 4. Create a turtle to act as the animation object
anim_turtle = turtle.Turtle()
anim_turtle.hideturtle()  # Hide the default turtle arrow shape
anim_turtle.penup()       # Lift the pen to prevent drawing lines

# 5. The animation loop
while True:
    for image in image_files:
        anim_turtle.shape(image)  # Change the turtle's shape
        screen.update()           # Manually refresh the screen to show the new image
        time.sleep(0.15)          # Pause to control the animation speed