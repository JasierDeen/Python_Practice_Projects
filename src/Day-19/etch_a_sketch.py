import turtle as t

tim = t.Turtle()
screen = t.Screen()
screen.listen()

def move_tim_forwards():
    tim.forward(10)

def move_tim_backwards():
    tim.backward(10)

def turn_tim_right():
    # tim.right(10) or tim.rt(10)
    tim.setheading(tim.heading() - 10)

def turn_tim_left():
    # tim.left(10) or tim.lt(10)
    tim.setheading(tim.heading() + 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkey(key="w", fun=move_tim_forwards)
screen.onkey(key="s", fun=move_tim_backwards)
screen.onkey(key="a", fun=turn_tim_left)
screen.onkey(key="d", fun=turn_tim_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
