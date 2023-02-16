import random
from turtle import Screen
from ball import Ball
from paddle import Paddle
from blocks import Blocks
from score import Score

colors = ["red", "white", "blue", "green", "cyan", "purple"]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
score = Score()

new_x = -340
for item in range(7):
    color = random.choice(colors)
    position = (new_x, 220)
    block = Blocks(color, position)
    new_x = new_x + 105

new_x = -340
for item in range(7):
    color = random.choice(colors)
    position = (new_x, 200)
    block = Blocks(color, position)
    new_x = new_x + 105

screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")



game_is_on = True
while game_is_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.xbounce()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.ybounce()

    if ball.distance(paddle) < 50 and ball.ycor() > -300:
        print("ball made contact with paddle")
        ball.xbounce()


    if ball.distance(block) < 50:
        print("made contact")
        block.hideturtle()
        ball.xbounce()
        score.update()

screen.exitonclick()

