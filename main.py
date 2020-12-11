from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width= 900, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(425)
l_paddle = Paddle(-425)
ball = Ball()
scoreboard = Scoreboard()
scoreboard.display()

rounds = int(screen.textinput("Pong", "First to:"))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
# time_sleep dictates the speed of the game
while game_on:
    time.sleep(ball.moves_speed)
    screen.update()
    ball.move()

    # detecting wall collision (top and bottom)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # detecting collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 400 or ball.distance(l_paddle) < 50 and ball.xcor() < -400:
        ball.hit()
    # detects when the paddle misses on the left
    elif ball.xcor() < -430:
        time.sleep(1)
        scoreboard.r_point()
        ball.miss()
    # detects when the paddle misses on the right
    elif ball.xcor() > 430:
        time.sleep(0.5)
        scoreboard.l_point()
        ball.miss()

    # stops the game when one of the users reaches 10
    if scoreboard.r_score > rounds or scoreboard.l_score > rounds:
        game_on = False
        scoreboard.game_over()






screen.exitonclick()
