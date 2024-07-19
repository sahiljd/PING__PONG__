import turtle
import random
import time

#Creating a screen
wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


score_a = 0
score_b = 0
chy = 50

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
#Position
paddle_a.goto(-350,0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
#Position
paddle_b.goto(350,0)

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
#Position
ball.goto(0,0)

ball.dx = random.choice([0.35,-0.35])
ball.dy = random.choice([0.35,-0.35])

def update_score():
    pen.clear()
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))


def gameOver():
    pen.clear()
    pen.goto(0,0)
    
    if score_a==10:
        pen.write(f"GAMEOVER\nPLAYER A Wins !!", align="center", font=("Courier", 24, "normal"))
        
    if score_b==10:
        pen.write(f"GAMEOVER\nPLAYER B Wins !!", align="center", font=("Courier", 24, "normal"))
    
    time.sleep(5)
    exit(0)
    
    
def paddle_a_up():
    #Current ycor
    y = paddle_a.ycor()
    if y>=250:
        paddle_a.sety(250)    
    else:
        y+=chy
        paddle_a.sety(y)
    
def paddle_a_down():
    #Current ycor
    y = paddle_a.ycor()
    if y<=-250:
        paddle_a.sety(-250)    
    else:
        y-=chy
        paddle_a.sety(y)

def paddle_b_up():
    #Current ycor
    y = paddle_b.ycor()
    if y>=250:
        paddle_b.sety(250)    
    else:
        y+=chy
        paddle_b.sety(y)
    
def paddle_b_down():
    #Current ycor
    y = paddle_b.ycor()
    if y<=-250:
        paddle_b.sety(-250)    
    else:
        y-=chy
        paddle_b.sety(y)




#Keyboard
#Listen to keyboard input
wn.listen()
#onkeypress of w activate paddle_a_up function
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')




#Main Game loop
while True:
    #Keep updating screen
    wn.update()
    
    #Move the ball
    
    #Set x cor to current position + ball.dx
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    if score_a==10 or score_b==10:
        gameOver()
    
    
    #Border for ball
    if ball.ycor() >= 290:
        ball.sety(290)
        ball.dy*=-1
    
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy*=-1
        
    if ball.xcor() >= 390:
        score_a += 1
        update_score()
        ball.goto(0,0)
        ball.dx*=-1
    
    if ball.xcor() <= -390:
        score_b += 1
        update_score()
        ball.goto(0,0)
        ball.dx*=-1    
    
    #Paddle and Ball Collision
    
    if (ball.dx > 0 and ball.xcor() > 340 and ball.xcor() < 350 and 
    (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50)):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.dx < 0 and ball.xcor() < -340 and ball.xcor() > -350 and 
        ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
        
    

    