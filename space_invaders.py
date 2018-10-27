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

# Player movement
playerspeed = 15

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
# Create keyboard bindings
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")






wn.mainloop()
