from turtle import *

cnt = 0
cnt2 = 'right'
cnt3 = 'left'


class Sprite(Turtle):
    def __init__(self, x, y, step=10, shape='circle', color='black'):
        super().__init__()
        self.penup()
        self.speed(0)
        self.goto(x, y)
        self.shape(shape)
        self.color(color)
        self.step = step

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)

    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def is_collide(self, waewae):
        if self.distance(waewae) < 20:
            return True

    def makestep(self, direction):
        if direction == 'left':
            self.move_left()
        elif direction == 'right':
            self.move_right()

    def setmove(self, type):
        global cnt2
        global cnt3
        if type == 1:
            if abs(self.xcor()) >= 200:
                if cnt2 == 'right':
                    cnt2 = 'left'
                else:
                    cnt2 = 'right'
            self.makestep(cnt2)
        else:
            if abs(self.xcor()) >= 200:
                if cnt3 == 'right':
                    cnt3 = 'left'
                else:
                    cnt3 = 'right'
            self.makestep(cnt3)


player = Sprite(0, -100, 10, 'circle', 'orange')
scr = player.getscreen()
enemy = Sprite(-190, 0, 10, 'square', 'red')
enemy2 = Sprite(190, 50, 10, 'square', 'red')
win = Sprite(10, 100, 10, 'triangle', 'green')
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_down, 'Down')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_left, 'Left')
while cnt != 3:
    if player.is_collide(enemy) == True or player.is_collide(enemy2) == True:
        player.hideturtle()
        win.hideturtle()
        break
    if player.is_collide(win) == True:
        cnt += 1
        player.goto(0, -100)
    enemy.setmove(1)
    enemy2.setmove(2)
enemy.hideturtle()
enemy2.hideturtle()

