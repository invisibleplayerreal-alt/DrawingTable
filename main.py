import turtle

ekran = turtle.Screen()
ekran.bgcolor("light blue")
ekran.title("turtle vektor")
ekran.tracer(0)

turtle123 = turtle.Turtle()
turtle123.shape("turtle")
turtle123.color("white")
turtle123.speed(0)
turtle123.pensize(3)

moving_forward = False
moving_backward = False
turning_left = False
turning_right = False


def start_forward():
    global moving_forward
    moving_forward = True


def stop_forward():
    global moving_forward
    moving_forward = False


def start_backward():
    global moving_backward
    moving_backward = True


def stop_backward():
    global moving_backward
    moving_backward = False


def start_left():
    global turning_left
    turning_left = True


def stop_left():
    global turning_left
    turning_left = False


def start_right():
    global turning_right
    turning_right = True


def stop_right():
    global turning_right
    turning_right = False


def clear_screen():
    turtle123.pendown()
    turtle123.clear()
    turtle123.penup()
    turtle123.home()
    turtle123.pendown()


def game_loop():
    if moving_forward:
        turtle123.forward(5)
    if moving_backward:
        turtle123.backward(5)
    if turning_left:
        turtle123.left(5)
    if turning_right:
        turtle123.right(5)

    ekran.update()
    ekran.ontimer(game_loop, 16)  # ~60 FPS


ekran.listen()

ekran.onkeypress(start_forward, key="Up")
ekran.onkeyrelease(stop_forward, key="Up")

ekran.onkeypress(start_backward, key="Down")
ekran.onkeyrelease(stop_backward, key="Down")

ekran.onkeypress(start_left, key="Left")
ekran.onkeyrelease(stop_left, key="Left")

ekran.onkeypress(start_right, key="Right")
ekran.onkeyrelease(stop_right, key="Right")

ekran.onkey(clear_screen, key="c")

game_loop()
turtle.done()