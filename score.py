from turtle import Turtle


class Score(Turtle):
    """docstring for Score."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('White')
        self.pu()
        self.goto(0, 275)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f'Score: {self.score}', align='center',
                   font=('Monaco', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!!!', align='center',
                   font=('Monaco', 12, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()
