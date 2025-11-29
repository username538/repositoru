from turtle import *
t = Turtle()
t.speed(100)
scr = t.getscreen()
t.color('blue')
t.shape('circle')
t.pensize(3)

cnt = 0
def draw(x,y):
    t.goto(x,y)
def screendraw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
def rightmove():
    t.goto(t.xcor() + 5,t.ycor())
def leftmove():
    t.goto(t.xcor() - 5,t.ycor())
def upmove():
    t.goto(t.xcor(),t.ycor() + 5)
def downmove():
    t.goto(t.xcor(),t.ycor() - 5)

def red():
    t.color('red')

def green():
    t.color('green')

def blue():
    t.color('blue')

def yellow():
    t.color('yellow')

def pink():
    t.color('pink')

def violet():
    t.color('violet')

def gray():
    t.color('gray')

def black():
    t.color('black')

def fill():
    global cnt
    if cnt == 0:
        t.begin_fill()
        cnt += 1
    elif cnt == 1:
        cnt = 0
        t.end_fill()
t.ondrag(draw)
scr.listen()
scr.onscreenclick(screendraw)
scr.onkey(rightmove,'Right')
scr.onkey(leftmove,'Left')
scr.onkey(upmove,'Up')
scr.onkey(downmove,'Down')
scr.onkey(fill,'f')
scr.onkey(red,'r')
scr.onkey(green,'e')
scr.onkey(blue,'t')
scr.onkey(yellow,'y')
scr.onkey(black,'u')
scr.onkey(gray,'i')
scr.onkey(violet,'o')
scr.onkey(pink,'p')
