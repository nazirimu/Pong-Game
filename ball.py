from turtle import Turtle



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.move_x = 10
        self.move_y = 10
        self.moves_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x,new_y)

    def bounce(self):
        self.move_y *= -1
        self.move()

    def hit(self):
        self.move_x *= -1
        self.moves_speed *= 0.8
        self.move()

    def miss(self):
        self.move_x *= -1
        self.move_y *= -1
        self.moves_speed = 0.05
        self.goto(0,0)
        self.move()




