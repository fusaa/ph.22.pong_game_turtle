from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.y = 0


    def up(self):
        self.y += 30
        self.sety(self.y)



    def down(self):
        self.y -= 30
        self.sety(self.y)



