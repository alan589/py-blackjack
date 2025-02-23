from turtle import Turtle, Screen

from settings import TEXT_BUTTON_FONT


class Button(Turtle):
    def __init__(self, x, y, text, color):
        screen = Screen()
        screen.tracer(0)
        super().__init__()

        self.hideturtle()
        self.penup()

        self.goto(x, y)
        self.pendown()
        self.begin_fill()
        self.color("black", color)
        self.pensize(3)
        self.forward(100)
        self.left(90)
        self.forward(40)
        self.left(90)
        self.forward(100)
        self.left(90)
        self.forward(40)
        self.left(90)
        self.end_fill()
        self.penup()


        self.goto(x + 53, y + 7)
        self.color("white")
        self.write(text, align="center", font=TEXT_BUTTON_FONT)


        screen.tracer(1)