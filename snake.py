from turtle import Turtle
POSITION = [(-20, 0), (-40, 0), (-60, 0), (-80, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    """Creates and controls the Snake."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the basic segments of the snake"""
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.penup()
        segment.color('whitesmoke')
        segment.shapesize(0.5)
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Controls the movement of the snake"""
        for seg in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[seg - 1].xcor()
            y_pos = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_pos, y_pos)
        self.head.forward(DISTANCE)

    def up(self):
        """Moves the snake upwards"""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Moves the snake downwards"""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        """Moves the snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        """Moves the snake to the right"""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
