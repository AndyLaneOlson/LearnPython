import turtle
#Set up my turtle and screen
wn = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(1)
myTurtle.pensize(8)
myTurtle.color("blue")
# myTurtle.penup()
# myTurtle.backward(400)
# myTurtle.pendown()

#Make the turtle do a triangle
for i in range(5):
    myTurtle.forward(126)
    myTurtle.left(216)