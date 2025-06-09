
import turtle
turtle.Screen().bgcolor("red")
turtle.Screen().title("spiral")

toortle = turtle.Turtle()

size = 0 
while True:
    for i in range(4):
        toortle.fd(size+1)
        toortle.left(90)
        size = size - 5
    size = size+1


