from turtle import Turtle, Screen

from settings import STACKED_POSITION


class Card(Turtle):
    def __init__(self, card_name, point):
        screen = Screen()
        screen.tracer(0)
        super().__init__()
        self.point = point
        self.shape(f"./assets/cards/{card_name}")
        self.speed(6)
        self.penup()
        self.goto(STACKED_POSITION)
        screen.tracer(1)

