from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xposition):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(xposition, 0)
        self.speed('fastest')

    def up(self):
        new_y = self.ycor() + 20
        old_x = self.xcor()
        self.goto(old_x,new_y)

    def down(self):
        new_y = self.ycor() - 20
        old_x = self.xcor()
        self.goto(old_x, new_y)
