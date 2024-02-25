import turtle

ground = turtle.Screen()
ground.bgpic("ground.png")
ground.addshape("right.gif")
ground.addshape("left.gif")
ground.addshape("ball.gif")

rightplayer = turtle.Turtle()
rightplayer.shape("right.gif")
rightplayer.penup()
rightplayer.goto(400,-200)

leftplayer = turtle.Turtle()
leftplayer.shape("left.gif")
leftplayer.penup()
leftplayer.goto(-400,200)

rightpen = turtle.Turtle()
rightpen.penup()
rightpen.hideturtle()
rightpen.goto(60,245)
rightpen.color("white")
rightpen.write("Rightplayer Score : 0",font=("Courier",23,"bold"))

leftpen = turtle.Turtle()
leftpen.penup()
leftpen.hideturtle()
leftpen.goto(-425,245)
leftpen.color("white")
leftpen.write("Leftplayer Score : 0",font=("Courier",23,"bold"))

ball = turtle.Turtle()
ball.penup()
ball.shape("ball.gif")
ball.speed(2000)

def leftplayerup():
    y = leftplayer.ycor()
    leftplayer.sety(y+10)
def leftplayerdown():
    y = leftplayer.ycor()
    leftplayer.sety(y-10)
def leftplayerleft():
    x = leftplayer.xcor()
    leftplayer.setx(x-10)
def leftplayerright():
    x = leftplayer.xcor()
    leftplayer.setx(x+10)
turtle.onkeypress(leftplayerup,"w")
turtle.onkeypress(leftplayerdown,"s")
turtle.onkeypress(leftplayerleft,"a")
turtle.onkeypress(leftplayerright,"d")


def rightplayerup():
    y = rightplayer.ycor()
    rightplayer.sety(y+10)
def rightplayerdown():
    y = rightplayer.ycor()
    rightplayer.sety(y-10)
def rightplayerleft():
    x = rightplayer.xcor()
    rightplayer.setx(x-10)
def rightplayerright():
    x = rightplayer.xcor()
    rightplayer.setx(x+10)
turtle.onkeypress(rightplayerup,"Up")
turtle.onkeypress(rightplayerdown,"Down")
turtle.onkeypress(rightplayerleft,"Left")
turtle.onkeypress(rightplayerright,"Right")


turtle.listen()

dx = 5
dy = -5
leftscore = 0
rightscore = 0

while True:
    x = ball.xcor()
    y = ball.ycor()
    ball.setpos(x+dx,y+dy)
    
    if rightplayer.distance(ball)<15:
        dx = -dx
        
    if leftplayer.distance(ball)<15:
        dx = -dx
        
    if ball.ycor() < -280:
        dy = -dy
        
    if ball.ycor() > 280:
        dy = -dy
        
    if ball.xcor() < -450:
        ball.goto(0,0)
        rightpen.clear()
        rightscore = rightscore + 1
        rightpen.write(("Rightplayer Score : {}").format(rightscore),font=("Courier",23,"bold"))
        
    if ball.xcor() > 450:
        ball.goto(0,0)
        leftpen.clear()
        leftscore = leftscore + 1
        leftpen.write(("Leftplayer Score : {}").format(leftscore),font=("Courier",23,"bold"))
        
turtle.done()