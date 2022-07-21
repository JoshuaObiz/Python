import random
from turtle import Turtle


class Food(Turtle):
    """docstring for Food."""

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('royalblue')
        self.penup()
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-330, 330)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)