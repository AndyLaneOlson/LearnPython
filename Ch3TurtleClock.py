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
for i in range(12):
    myTurtle.penup()
    myTurtle.forward(120)
    myTurtle.pendown()
    myTurtle.forward(20)
    myTurtle.penup()
    myTurtle.forward(20)
    myTurtle.stamp()
    myTurtle.backward(160)
    myTurtle.left(30)

wn.mainloop()
