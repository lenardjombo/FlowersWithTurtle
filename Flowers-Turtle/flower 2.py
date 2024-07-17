import turtle
t = turtle.Turtle()
t.screen.bgcolor('black')
for i in range (180):
    t.speed(0)
    t.color('#277BC0')
    t.circle(190 - i, 90)
    t.left(90)
    t.color('#E38B29')
    t.circle(190 - i, 90)
    t.left(18)
