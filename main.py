import turtle
import random
# import  winsound


# Create Screen
wn = turtle.Screen()
wn.bgcolor('black')
wn.title('SPACE GAME')
wn.tracer(0)
wn.setup(width=800, height=600)
player1_life = 3
player_life = 3

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.write("Player A:{}  Player B:{}".format(player_life, player1_life), align='center', font=('Courier', 15, 'normal'))


class Missile(turtle.Turtle):
    def __init__(self, color):
        turtle.Turtle.__init__(self)
        self.goto(0, 0)
        self.ht()
        self.shape('triangle')
        self.shapesize(0.1, 0.3)
        self.width(2)
        self.shot = "no"
        self.color(color)
        self.speed(0)
        self.penup()
        self.velocity = 0

    def move(self):
        if self.shot == 'yes':
            self.fd(self.velocity)


M = Missile('white')
M1 = Missile('blue')


# Creating Sprites
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty, name):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.Name = name
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.velocity = 0.4

    def turn_left(self):
        self.lt(45)

    def move(self):
        self.fd(self.velocity)

    def turn_right(self):
        self.rt(45)

    def bounds(self):
        # Boundary Check

        if self.ycor() > 275:
            if self.Name == 'a':
                self.goto(random.randrange(-350, 350), random.randrange(-250, 250))
            else:
                self.sety(275)
        if self.xcor() > 370:
            if self.Name == 'a':
                self.goto(random.randrange(-350, 350), random.randrange(-250, 250))
            else:
                self.setx(370)
        if self.ycor() < -270:
            if self.Name == 'a':
                self.goto(random.randrange(-350, 350), random.randrange(-250, 250))
            else:
                self.sety(-270)
        if self.xcor() < -370:
            if self.Name == 'a':
                self.goto(random.randrange(-350, 350), random.randrange(-250, 250))
            else:
                self.setx(-370)

    def shoot(self):
        if self.Name == 'player1':
            M1.st()
            M1.goto(player1.xcor(), player1.ycor())
            M1.setheading(player1.heading())
            M1.velocity = 2
            M1.shot = 'yes'
        if self.Name == 'player':
            M.st()
            M.goto(player.xcor(), player.ycor())
            M.setheading(player.heading())
            M.velocity = 2
            M.shot = 'yes'


# Player 1
player = Sprite('triangle', 'white', -250, 0, 'player')
player.velocity = 0.8
player.shapesize(1, 2)

# Player 2
player1 = Sprite('triangle', 'blue', 250, 0, 'player1')
player1.velocity = 0.8
player1.shapesize(1, 2)


# Enemy Sprites
s = [Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a'),
     Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a'),
     Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a'),
     Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a'),
     Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a'),
     Sprite('triangle', 'red', random.randrange(-350, 350), random.randrange(-260, 260), 'a')]


# Keyboard Binding
wn.listen()
wn.onkeypress(player.turn_left, 'Left')
wn.onkeypress(player.turn_right, 'Right')
wn.onkeypress(player1.turn_left, 'a')
wn.onkeypress(player1.turn_right, 'd')
wn.onkeypress(player.shoot, 'Down')
wn.onkeypress(player1.shoot, 's')
wn.listen()

def game_over():
    pen.clear()
    player1.ht()
    player.ht()
    if player1_life < player_life:
        pen.write("   GAME OVER \n PLAYER WHITE WINS", align='center', font=('Courier', 20, 'normal'))
    else:
        pen.write("   GAME OVER \n PLAYER BLUE WINS", align='center', font=('Courier', 20, 'normal'))


# main
while True:
    wn.update()
    player.move()
    player.bounds()
    player1.move()
    player1.bounds()
    M.move()
    M1.move()

    # Assigns enemy movements
    for i in range(6):
        s[i].move()
        s[i].rt(random.randrange(-1.0, 4.0))
        s[i].bounds()
        # checks for collisions
        if (player.xcor()-s[i].xcor())**2 + (player.ycor()-s[i].ycor())**2 <= 400:
            s[i].goto(500, 500)
            player_life -= 1
            pen.clear()
            pen.write("Player A:{}  Player B:{}".format(player_life, player1_life), align='center',
                      font=('Courier', 15, 'normal'))

        if (player1.xcor() - s[i].xcor()) ** 2 + (player1.ycor() - s[i].ycor()) ** 2 <= 400:
            s[i].goto(500, 500)
            player1_life -= 1
            pen.clear()
            pen.write("Player A:{}  Player B:{}".format(player_life, player1_life), align='center',
                      font=('Courier', 15, 'normal'))

        if (M.xcor() - s[i].xcor()) ** 2 + (M.ycor() - s[i].ycor()) ** 2 <= 400:
            s[i].goto(500, 500)
        if (M1.xcor() - s[i].xcor()) ** 2 + (M1.ycor() - s[i].ycor()) ** 2 <= 400:
            s[i].goto(500, 500)

    if (player.xcor() - M1.xcor()) ** 2 + (player.ycor() - M1.ycor()) ** 2 <= 400:
        M1.goto(-500,500)
        player_life -= 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(player_life, player1_life), align='center',
                  font=('Courier', 15, 'normal'))

    if (player1.xcor() - M.xcor()) ** 2 + (player1.ycor() - M.ycor()) ** 2 <= 400:
        M.goto(-500, 500)
        player1_life -= 1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(player_life, player1_life), align='center',
                  font=('Courier', 15, 'normal'))

    if player_life < 1 or player1_life < 1:
        game_over()

        # Collisions with enemy
    wn.delay(100)
