from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.mode("logo")
screen.bgcolor("black")
screen.tracer(0)
screen.title("Pong")



paddle_r = Paddle()
paddle_r.goto(350,0)

paddle_l = Paddle()
paddle_l.goto(-350,0)

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")

score=Score()
ball=Ball()
ball_x = 0
ball_y = 0
ball_speed = 3
BALL_SPEED = 3

ascending = True
is_left = False
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.02)

    # Ball animation:
    if ascending == True:
        if is_left == False:
            ball_x += ball_speed
        else:
            ball_x -= ball_speed
        ball_y += ball_speed
        ball.goto(ball_x,ball_y)
    if ball_y > 280:
        ascending = False
    if ascending == False:
        if is_left == False:
            ball_x += ball_speed
        else:
            ball_x -= ball_speed
        ball_y -= ball_speed
        ball.goto(ball_x,ball_y)
    if ball_y <= -280:
        ascending = True

    if ball.distance(paddle_r) <= 50 or ball.distance(paddle_l) <= 50:
        if ball_x > 330: is_left = True
        if ball_x < -330: is_left = False
        ball_speed += .1
    elif ball_x >= 330 or ball_x <= -330:
        print("Point")
        if ball_x > 200:
            is_left = True
            score.left()
            ball_speed = BALL_SPEED
        if ball_x < -200:
            is_left = False
            score.right()
            ball_speed = BALL_SPEED
        ball_x = 0
        ball_y = 0













screen.exitonclick()