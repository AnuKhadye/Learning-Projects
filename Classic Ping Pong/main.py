from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen Settings 
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Classic Pong game!!")
screen.tracer(0)
 
# Object Declaration   
l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()
    
# To Move resepective paddles
screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")

screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()
    
    # Detcting Collisions with the top and the bottom screen
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
        
    # Detecting collisions with the paddles    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 322 or ball.distance(l_paddle) < 50 and ball.xcor() < -322:
        ball.bounce_x()
        
    # Reseting the ball's postion when it goes out of bounds.
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.left_score()

        
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_score()
        

    
        
screen.exitonclick()
