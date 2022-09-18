from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.y = 220
        self.l = -100
        self.r = 100
        self.score_l = 0
        self.score_r = 0
        self.update()


    def left(self):
        self.score_l += 1
        self.update()

    def right(self):
        self.score_r += 1
        self.update()

    def update(self):
        self.clear()
        self.goto(self.l, self.y)
        self.write(self.score_l, align="center", font=("Courier",60,"normal"))
        self.goto(self.r, self.y)
        self.write(self.score_r, align="center", font=("Courier",60,"normal"))


