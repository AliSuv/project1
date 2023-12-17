import turtle as t

pen = t.Turtle()
t.bgcolor("black")
pen.speed(1)
pen.color("red")
pen.fillcolor("white")
pen.width(4)

pen.up()
pen.goto(-50, 0)

pen.down()
for i in range(2):
    pen.begin_fill()
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.forward(200)

    pen.down()

pen.circle(20)

t.done()