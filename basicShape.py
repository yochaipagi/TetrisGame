# basicShape.py
from turtle import Turtle


class BasicShape(Turtle):
    def __init__(self, x, y, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.goto(x, y)
