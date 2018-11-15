# Space Invaders
import turtle
import math
import random
import winsound

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("#000")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

# Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
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

# Set the score to 0
score = 0

# Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("#fff")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 13, "normal"))
score_pen.hideturtle()

# Game over pen
game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("#fff")
game_over_pen.penup()
game_over_pen.setposition(-25, 0)
game_over_string = ""
game_over_pen.write(game_over_string, False, align="center", font=("Arial", 13, "normal"))
game_over_pen.hideturtle()


# Create the player Turtle
player = turtle.Turtle()
player.color("#00f")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)


playerspeed = 15


# Choose a number of enemies
number_of_enemies = 5
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(number_of_enemies):
    # Create enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("#f00")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

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
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        bulletstate = "fire"
        # Move the bullet to just above the player
        bullet.setposition(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def isCollision(t1, t2): # t for turtle
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    return distance < 15


# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeypress(fire_bullet, "space")
# Main game loop
while True:
    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        broke = False

        # Move enemy back and down
        if x > 280:
            # Move all enemies down
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            # change enemy direction
            enemyspeed *= -1

        if x < -280:
            for enemy in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            enemyspeed *= -1

        # Check for a collision between bullet and enemy
        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion", winsound.SND_ASYNC)
            # Reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400) # To prevent collision with other enemies
            # Reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            # Update the score
            score += 1
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 13, "normal"))


        # Check for a collision between player and enemy
        if isCollision(player, enemy) or enemy.ycor() < -250:
            broke = True
            winsound.PlaySound("explosion", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            game_over_string = "Game Over"
            game_over_pen.write(game_over_string, False, align="left", font=("Arial", 13, "normal"))
            break


    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


    if broke:
        break


wn.mainloop()
