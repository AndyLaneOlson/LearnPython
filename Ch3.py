import turtle




msg = "We like Python's turtles!"
for i in range(999):
    print(msg)

# Cellphone Attributes: Weight, Color, Size
# Cellphone methods: Call(), HangUp(), VolumeUp()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for m in months:
    print("One of the months of the year is " + m)

xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in xs:
    print(str(i))

for i in xs:
    #answer = i**
    print(i ** 2) 

total = 0
for i in xs:
    total = total + i
print("\n")
print(total)

total = 0
for i in xs:
    total = total * i

# question 9
# 20 degrees

newTurtle = turtle.Turtle()
print(type(newTurtle))
