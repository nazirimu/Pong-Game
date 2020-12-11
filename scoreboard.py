from turtle import Turtle

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.winner = ''

    def display(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.display()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.display()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        if self.r_score < self.l_score:
            self.winner = "Left"
        else:
            self.winner = "right"
        self.write(f'The winner is {self.winner}', align="center", font=("Courier", 20, "normal"))


