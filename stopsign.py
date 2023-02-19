import turtle

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
turtle.penup()
turtle.goto(-50, 120)
turtle.pendown()

for count in range(NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

turtle.penup()
turtle.goto(-50, 115)
turtle.pendown()

LENGTH = 95

turtle.begin_fill()
turtle.fillcolor('red')
turtle.pencolor('red')

for x in range (NUM_SIDES):
    turtle.forward(LENGTH)
    turtle.right(ANGLE)

turtle.end_fill()

style = ('Highway Gothic', 60, 'bold')

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()

turtle.color('white')
turtle.write('STOP', font = style, align = 'center')
