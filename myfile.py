import turtle 
import time 

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Michael Jackson")

butterfly_frames = ["A.gif", "B.gif", "C.gif", "D.gif"]

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
    time.sleep(0.25)

turtle.done()




