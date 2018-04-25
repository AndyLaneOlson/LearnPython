import turtle
#Set up my turtle and screen
wn = turtle.Screen()
myTurtle = turtle.Turtle()
myTurtle.shape("turtle")
myTurtle.speed(1)
myTurtle.pensize(8)
myTurtle.color("blue")
myTurtle.penup()
myTurtle.backward(400)
myTurtle.pendown()

#Make the turtle do a triangle
for i in range(3):
    myTurtle.forward(100)
    myTurtle.left(120)

#Move the turtle to a new spot
myTurtle.penup()
myTurtle.forward(200)
myTurtle.pendown()

#Make the turtle create a square
for i in range(4):
    myTurtle.forward(100)
    myTurtle.left(90)

myTurtle.penup()
myTurtle.forward(200)
myTurtle.pendown()

#Make the turtle create a hexagon
for i in range(6):
    myTurtle.forward(60)
    myTurtle.left(60)

myTurtle.penup()
myTurtle.forward(200)
myTurtle.pendown()

#Make the turtle create an octagon
for i in range(8):
    myTurtle.forward(50)
    myTurtle.left(45)

wn.mainloop()
