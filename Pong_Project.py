import turtle

root=turtle.Screen()
root.bgcolor("Navy blue")
root.title("Pong Game")
root.setup(width=800,height=600)
root.tracer(2)

#paddle_a
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle_b

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player 1 and player 2",align="center",font=("Courier",24,"normal"))
#pen.write(())
score_a = 0
score_b = 0

#paddle_a_move

def paddle_a_up():
    y=paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

#Similarly_for_paddle_b_move
def paddle_b_up():
    y=paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard bild
root.listen()
root.onkeypress(paddle_a_up,"w")
root.onkeypress(paddle_a_down,"x")
root.onkeypress(paddle_b_up,"o")
root.onkeypress(paddle_b_down,"k")

while(True):
    root.update()
    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

#When_ball_Touch_the_border_hit_the_ball

    if ball.ycor()> 290:
     ball.sety(290)
     ball.dy *= -1


    if ball.ycor() < -290:
     ball.sety(-290)
     ball.dy *= -1

    if ball.xcor() > 390:
     ball.goto(0,0)
     ball.dx *= -1
     score_a += 1
     pen.clear()
     pen.write("Player A :{} Player B:{}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    if ball.xcor() < -390:
     ball.goto(0,0)
     ball.dx *= -1
     score_b += 1
     pen.clear()
     pen.write("Player A :{} Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

     #if(ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor() +40 and ball.ycor()>paddle_b.ycor()-40):
      #ball.setx(340)
      #ball.dx*= -1

     #if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
    #  ball.setx(-340)
    #  ball.dx *= -1
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40:
        ball.dx *= -1


    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40:
        ball.dx *= -1

turtle.exitonclick()
