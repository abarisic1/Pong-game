from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)    
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collisions with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()
        
    # Detect miss from R paddle
    if ball.xcor() > 380:
        ball.miss()
        scoreboard.l_point()

    # Detect miss from L paddle 
    if ball.xcor() < -380:
        ball.miss()
        scoreboard.r_point()
        




screen.exitonclick()

