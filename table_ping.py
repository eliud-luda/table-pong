# a table surface game to hit ball upwards

import turtle

# make window
wn = turtle.Screen()
wn.title('Surface Ping')
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)


# paddle
paddle = turtle.Turtle()
paddle.speed(1) # animation speed
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=1,stretch_len=6)
paddle.penup()
paddle.goto(0,-250)

# table
table = turtle.Turtle()
table.speed(1) # animation speed
table.shape('square')
table.color('white')
table.shapesize(stretch_wid=1,stretch_len=40)
table.penup()
table.goto(0,250)

# ball
# ball
ball = turtle.Turtle()
ball.speed(1) # animation speed
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.7
ball.dy = 0.7

def paddle_left():
    global paddle
    y = paddle.xcor()
    y -= 20
    paddle.setx(y)


def paddle_right():
    global paddle
    y = paddle.xcor()
    y += 20
    paddle.setx(y)

def ball_move_border_check():
    global ball,table
    # move the ball
    ball.setx(ball.xcor() + ball.dx )
    ball.sety(ball.ycor() + ball.dy )


    # check left right bottom border:
    
    # right
    if ball.xcor() > 390:
        ball.dx *= -1

    #left
    if ball.xcor() < -390:
        ball.dx *= -1  
    
    # bottom
    if ball.ycor() < -300:
        ball.goto(0,0)

        
    
def ball_table_collision():
    global ball, table

    # table ball collision
    if ball.ycor() > table.ycor():
        ball.dy *= -1

    

def ball_paddle_collision():
    global ball, paddle
    #ball paddle collision
    while ball.ycor() < -249:
        if ball.ycor() > paddle.ycor():
            ball.dy *= -1
        

    
def paddle_move():
    global wn,paddle_left,paddle_right
    wn.listen()
    # paddle a up or down
    wn.onkeypress(paddle_left,'Left')
    wn.onkeypress(paddle_right,'Right')
  

is_on = True

while is_on:
    wn.update()

    ball_move_border_check()
    ball_table_collision()
    ball_paddle_collision()
    paddle_move()