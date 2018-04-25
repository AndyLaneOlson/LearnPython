import turtle
wn = turtle.Screen()
pirate = turtle.Turtle()
pirate.pensize(8)
pirate.color("red")
pirate.speed(1)
pirateHeading = 0
drunkSteps = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in drunkSteps:
    pirateHeading = pirateHeading + i
    pirate.left(i)
    pirate.forward(100)

print(i)
wn.mainloop()