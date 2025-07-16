import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Flying Butterfly")

butterfly_frames = ["6.png", "7.png", "8.png", "9.png"]


for frame in butterfly_frames:
    screen.addshape(frame)


butterfly = turtle.Turtle()
butterfly.penup()
butterfly.speed("fastest")
butterfly.goto(-screen.window_width() // 2, 0) 

frame_index = 0
while butterfly.xcor() < screen.window_width() // 2: 
    butterfly.shape(butterfly_frames[frame_index])
    frame_index = (frame_index + 1) % len(butterfly_frames)
    butterfly.forward(15)
    screen.update()
    time.sleep(0.05)

turtle.done()