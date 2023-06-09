import turtle
import os
import winsound
#Defaults
window = turtle.Screen()
window.title("Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)
#Score
score_1 = 0
score_2 = 0

#Paddle 1
paddle_one = turtle.Turtle()
paddle_one.speed(0)
paddle_one.shape("square")
paddle_one.color("red")
paddle_one.shapesize(stretch_wid=5, stretch_len=1, outline=17)
paddle_one.penup()
paddle_one.goto(-350, 0)
#Paddle 2
paddle_two = turtle.Turtle()
paddle_two.speed(0)
paddle_two.shape("square")
paddle_two.color("red")
paddle_two.shapesize(stretch_wid=5, stretch_len=1, outline=17)
paddle_two.penup()
paddle_two.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#Text
txt = turtle.Turtle()
txt.speed(0)
txt.color("red")
txt.penup()
txt.hideturtle()
txt.goto(0, 260)
txt.write("Player 1: 0  Player 2: 0", align="center", font=("Arial", 15, "normal"))

#Function
def paddle_one_up():
    y = paddle_one.ycor()
    y += 20
    paddle_one.sety(y)

def paddle_one_down():
    y = paddle_one.ycor()
    y -= 20
    paddle_one.sety(y)

def paddle_two_up():
    y = paddle_two.ycor()
    y += 20
    paddle_two.sety(y)

def paddle_two_down():
    y = paddle_two.ycor()
    y -= 20
    paddle_two.sety(y)
#Keyboard
window.listen()
window.onkeypress(paddle_one_up, "w")
window.onkeypress(paddle_one_down, "s")
window.onkeypress(paddle_two_up, "Up")
window.onkeypress(paddle_two_down, "Down")

#Game
while True:
    window.update()


    #Move Ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/jump.wav', winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/jump.wav', winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        txt.clear()
        txt.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 15, "normal"))
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/point.wav', winsound.SND_ASYNC)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        txt.clear()
        txt.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center", font=("Arial", 15, "normal"))
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/point.wav', winsound.SND_ASYNC)


    #Collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_two.ycor() + 50 and ball.ycor() > paddle_two.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/jump.wav', winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_one.ycor() + 50 and ball.ycor() > paddle_one.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/Arymzn/OneDrive/Desktop/Projects/Pong/jump.wav', winsound.SND_ASYNC)


    #Game Over
    if score_1 == 5:
        turtle.clearscreen()
        txt.goto(0, 0)
        turtle.tracer(False)
        txt.write("Game Over, Player 1 won", align="center", font=("Arial", 30, "normal"))
    if score_2 == 5:
        turtle.clearscreen()
        txt.goto(0, 0)
        turtle.tracer(False)
        txt.write("Game Over, Player 2 won", align="center", font=("Arial", 30, "normal"))
