import turtle
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(300)
colors = ['red','darkred']
for number in range (400):
    t.forward(number +1)
    t.right(89)
    t.pencolor(colors[number%2])
turtle.done()