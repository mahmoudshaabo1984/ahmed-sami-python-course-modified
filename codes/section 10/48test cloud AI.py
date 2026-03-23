

import turtle # Imports the turtle library to create graphics
import time  # Import the time module to pause the game loop

# Create a window (screen) object
wind = turtle.Screen() # Initializes a new screen object
wind.title("Ping Pong By Codezilla") # Sets the title of the window
wind.bgcolor("black") # Sets the background color of the window
wind.setup(width=800, height=600) # Sets the size of the window
wind.tracer(0) # Turns off automatic screen updates for faster performance

# Madrab 1 (Left Paddle)
madrab1 = turtle.Turtle() # Creates a turtle object for the first paddle
madrab1.speed(0) # Sets the animation speed to the fastest
madrab1.shape("square") # Sets the shape of the object
madrab1.color("blue") # Sets the color of the paddle
madrab1.shapesize(stretch_wid=5, stretch_len=1) # Stretches the shape to make it a rectangle
madrab1.penup() # Lifts the turtle's pen to not draw a line when moving
madrab1.goto(-350, 0) # Moves the paddle to its starting position on the left

# Madrab 2 (Right Paddle)
madrab2 = turtle.Turtle() # Creates a turtle object for the second paddle
madrab2.speed(0) # Sets the animation speed to the fastest
madrab2.shape("square") # Sets the shape of the object
madrab2.color("red") # Sets the color of the paddle
madrab2.shapesize(stretch_wid=5, stretch_len=1) # Stretches the shape to make it a rectangle
madrab2.penup() # Lifts the turtle's pen to not draw a line when moving
madrab2.goto(350, 0) # Moves the paddle to its starting position on the right

# Ball
ball = turtle.Turtle() # Creates a turtle object for the ball
ball.speed(0) # Sets the animation speed to the fastest
ball.shape("square") # Sets the shape of the object
ball.color("white") # Sets the color of the ball
ball.penup() # Lifts the turtle's pen to not draw a line when moving
ball.goto(0, 0) # Moves the ball to the center of the screen
ball.dx = 1.5 # Sets the ball's horizontal movement speed (delta-x)
ball.dy = 1.5 # Sets the ball's vertical movement speed (delta-y)

# Functions to move the paddles
def madrab1_up():
    y = madrab1.ycor() # Gets the current y-coordinate of paddle 1
    y += 20 # Increases the y-coordinate by 20 pixels
    madrab1.sety(y) # Sets the new y-coordinate for paddle 1

def madrab1_down():
    y = madrab1.ycor() # Gets the current y-coordinate of paddle 1
    y -= 20 # Decreases the y-coordinate by 20 pixels
    madrab1.sety(y) # Sets the new y-coordinate for paddle 1

def madrab2_up():
    y = madrab2.ycor() # Gets the current y-coordinate of paddle 2
    y += 20 # Increases the y-coordinate by 20 pixels
    madrab2.sety(y) # Sets the new y-coordinate for paddle 2

def madrab2_down():
    y = madrab2.ycor() # Gets the current y-coordinate of paddle 2
    y -= 20 # Decreases the y-coordinate by 20 pixels
    madrab2.sety(y) # Sets the new y-coordinate for paddle 2

# Keyboard bindings
wind.listen() # Tells the window to listen for keyboard input
wind.onkeypress(madrab1_up, "w") # Binds the 'w' key to the madrab1_up function
wind.onkeypress(madrab1_down, "s") # Binds the 's' key to the madrab1_down function
wind.onkeypress(madrab2_up, "Up") # Binds the 'Up Arrow' key to the madrab2_up function
wind.onkeypress(madrab2_down, "Down") # Binds the 'Down Arrow' key to the madrab2_down function

# Main game loop
while True:
    wind.update() # Manually updates the screen in each loop cycle
    time.sleep(0.01) # Pause the loop for a short time to control the game speed
    

    # Move the ball
    ball.setx(ball.xcor() + ball.dx) # Moves the ball horizontally based on its dx speed
    ball.sety(ball.ycor() + ball.dy) # Moves the ball vertically based on its dy speed

    # Border checking (Top and Bottom walls)
    if ball.ycor() > 290: # Checks if the ball hit the top border
        ball.sety(290) # Resets the ball's position to the border
        ball.dy *= -1 # Reverses the ball's vertical direction (bounces)

    if ball.ycor() < -290: # Checks if the ball hit the bottom border
        ball.sety(-290) # Resets the ball's position to the border
        ball.dy *= -1 # Reverses the ball's vertical direction (bounces)

    # Border checking (Left and Right walls / scoring)
    if ball.xcor() > 390: # Checks if the ball went past the right paddle
        ball.goto(0, 0) # Resets the ball to the center
        ball.dx *= -1 # Reverses the horizontal direction to serve to the other player

    if ball.xcor() < -390: # Checks if the ball went past the left paddle
        ball.goto(0, 0) # Resets the ball to the center
        ball.dx *= -1 # Reverses the horizontal direction to serve to the other player