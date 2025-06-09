
import turtle 
turtle.Screen().bgcolor("gold")
turtle.Screen().setup(300, 400)
toortle = turtle.Turtle()

num_of_sides = int(input("enter the number of sides:- "))
side_lenght = int(input("enter the side lenght:- "))
angle = 360.0/num_of_sides

for i in range(num_of_sides):
    toortle.forward(side_lenght)
    toortle.right(angle)


turtle.done()

