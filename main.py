from turtle import Screen
from paddle import Paddle
import time
from score import Score
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ponging")
screen.tracer(0)

right_paddle = Paddle((380, 0))
left_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

game_on = True
speed = 0.1


while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(right_paddle) < 50
        and ball.xcor() > 360
        or ball.distance(left_paddle) < 50
        and ball.xcor() < -360
    ):
        ball.bounce_x()
        speed *= 0.9

    if ball.xcor() > 380:
        ball.reset()
        score.left_scores()
        speed = 0.1

    if ball.xcor() < -380:
        ball.reset()
        score.right_scores()
        speed = 0.1


screen.exitonclick()
