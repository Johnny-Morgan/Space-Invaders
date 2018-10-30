# Space Invaders
import turtle

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("#000")
wn.title("Space Invaders")

# Draw border
border_pen = turtle.Turtle() # Turtle object
border_pen.speed(0) # 0 is fastest speed we can go
border_pen.color("#fff")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600) # forward
    border_pen.lt(90) # left
border_pen.hideturtle()

# Create the player Turtle
player = turtle.Turtle()
player.color("#00f")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


playerspeed = 15

# Create enemy
enemy = turtle.Turtle()
enemy.color("#f00")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)
enemyspeed = 2

# Create the player's bullet
bullet = turtle.Turtle()
bullet.color("#ff0")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

# Define bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Move player left & right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare bulletstate as a global variables
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet to just above the player
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")
# Main game loop
while True:

    # Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)
    y = enemy.ycor()
    # Move enemy back and down
    if x > 280:
        enemyspeed *= -1
        y -= 40
        enemy.sety(y)

    if x < -280:
        enemyspeed *= -1
        y -= 40
        enemy.sety(y)

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"






wn.mainloop()
