import turtle as t
import time
from threading import Timer

pen = t.Turtle()
t.bgcolor("black")
pen.color("red")
pen.speed(2)

def draw_triangle():
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    clear()
    timer = Timer(2, draw_square)
    timer.start()

def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    clear()
    timer = Timer(2, draw_hexa)
    timer.start()

def draw_hexa():
    for i in range(6):
        pen.forward(100)
        pen.left(60)
    clear()

def clear():
    pen.clear()
    pen.up()
    pen.goto(0, 0)
    pen.down()

timer = Timer(2, draw_triangle)
timer.start()

t.done()

# ukol - nakreslit cokoli chces napr. domecek
# vse do nejmensiho prostoru (do cyklu)