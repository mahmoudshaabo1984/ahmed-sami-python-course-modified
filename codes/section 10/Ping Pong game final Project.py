import turtle  # Import the turtle graphics library
import time # Import the time module to pause the game loop

# Create a window (screen) object
screen = turtle.Screen() # Create a window/screen object for the game
screen.title("Ping Pong By Mahmoud Shaabo") # Set the window title
screen.bgcolor("black") # Set the background color to black
screen.setup(width=800 , height=600) # Set window dimensions: 800 pixels wide, 600 pixels high
screen.tracer(0) # Turn off automatic screen updates for better performance


# paddle 1 (Left Paddle)
left_paddle = turtle.Turtle()  # Create a turtle object for the first paddle
left_paddle.speed(0) # Set animation speed to maximum (0 = fastest)
left_paddle.shape("square") # Set the shape to square
left_paddle.color("blue") # Set the color to blue
left_paddle.shapesize(stretch_wid=5 ,stretch_len=1) # Stretch the square to form a paddle
left_paddle.penup() # Lift the pen to avoid drawing lines when moving
left_paddle.goto(-350,0) # Position the paddle on the left side


# paddle 2 (Right Paddle)
right_paddle = turtle.Turtle() # Create a turtle object for the second paddle
right_paddle.speed(0) # Set animation speed to maximum
right_paddle.shape("square") # Set the shape to square
right_paddle.color("red") # Set the color to red
right_paddle.shapesize(stretch_wid=5, stretch_len=1) # Stretch the square to form a paddle
right_paddle.penup() # Lift the pen to avoid drawing lines
right_paddle.goto(350, 0) # Position the paddle on the right side



# ball
ball = turtle.Turtle()# Create a turtle object for the ball
ball.speed(0) # Set animation speed to maximum
ball.shape("square") # Set the shape to square
ball.color("white") # Set the color to white
ball.penup() # Lift the pen to avoid drawing lines
ball.goto(0, 0) # Position the ball at the center
ball.dx = 1.5# Set ball's horizontal speed (pixels per frame)
ball.dy = 1.5 # Set ball's vertical speed (pixels per frame)


# Score
score1 = 0 # Variable to store player 1's score
score2 = 0 # Variable to store player 2's score
score = turtle.Turtle() # Create a turtle object for the scoreboard
score.speed(0) # Set animation speed to maximum
score.color("white") # Set the text color to white
score.penup() # Lift the pen to avoid drawing lines
score.hideturtle() # Hide the turtle object, we only need the text
score.goto(0, 260) # Position the scoreboard at the top center


# Write the initial score on the screen
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))




# functions
def left_paddle_up(): # Define function to move left_paddle up
    y = left_paddle.ycor() # Get the current y coordinate of  left_paddle
    y += 20 # Increase y by 20 pixels
    left_paddle.sety(y) # Set left_paddle's new y position


def left_paddle_down(): # Define function to move left_paddle down
    y = left_paddle.ycor() # Get the current y coordinate of left_paddle
    y -= 20 # Decrease y by 20 pixels
    left_paddle.sety(y) # Set left_paddle's new y position



def right_paddle_up():# Define function to move right_paddle 2 up
    y = right_paddle.ycor() # Get the current y coordinate of right_paddle 2
    y += 20 # Increase y by 20 pixels
    right_paddle.sety(y) # Set right_paddle's new y position




def right_paddle_down(): # Define function to move right_paddle 2 down
    y = right_paddle.ycor() # Get the current y coordinate of right_paddle 2
    y -= 20 # Decrease y by 20 pixels
    right_paddle.sety(y) # Set right_paddle2's new y position



# keyboard bindings
screen.listen() # Tell the window to listen for keyboard input
screen.onkeypress(left_paddle_up, "w")  # When 'w' key is pressed, call left_paddle_up function
screen.onkeypress(left_paddle_down, "s") # When 's' key is pressed, call  left_paddle_down function
screen.onkeypress(right_paddle_up, "Up") # When 'Up' arrow key is pressed, call right_paddle_up function
screen.onkeypress(right_paddle_down, "Down")  # When 'Down' arrow key is pressed, call  right_paddle_down function





# main game loop
while True: # Infinite loop to keep the game running
    screen.update() # Manually update the screen to reflect any changes (since tracer is off
    time.sleep(0.01) # Pause the loop for a short time to control the game speed

    # move the ball
    ball.setx(ball.xcor() + ball.dx)  # Move ball horizontally: current x position + dx
    ball.sety(ball.ycor() + ball.dy) # Move ball vertically: current y position + dy

    
    # border check
    if ball.ycor() > 290:  # Check if ball hit the top border (y > 290
        ball.sety(290) # Keep ball at the border position
        ball.dy *= -1 # Reverse vertical direction (bounce)
    
    if ball.ycor() < -290:  # Check if ball hit the bottom border (y < -290)
        ball.sety(-290) # Keep ball at the border position
        ball.dy *= -1 # Reverse vertical direction (bounce)



    if ball.xcor() > 390: # Check if ball passed the right border (missed by player 2)
        ball.goto(0, 0) # Reset ball to center position
        ball.dx *= -1 # Reverse horizontal direction
        score1 += 1 # Add a point to Player 1
        score.clear() # Clear the old score from the screen
        # Update the score display with the new scores
        score.write(f"Player 1: {score1} Player 2: {score2}", align="center", font=("Courier", 24, "normal"))
        
        
        
    if ball.xcor() < -390:  # Check if ball passed the left border (missed by player 1)
        ball.goto(0, 0) # Reset ball to center position
        ball.dx *= -1 # Reverse horizontal direction
        score2 += 1 # Add a point to Player 2
        score.clear() # Clear the old score from the screen
        # Update the score display with the new scores
        score.write(f"Player 1: {score1} Player 2: {score2}", align="center", font=("Courier", 24, "normal"))


# Check for collision with the left paddle (left_paddle)
    # It checks if the ball is within the horizontal and vertical range of the paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < left_paddle.ycor() + 40 and ball.ycor() > left_paddle.ycor() - 40):
        ball.setx(-340)     # Move the ball to the paddle's surface to prevent it from getting stuck
        ball.dx *= -1       # Reverse the ball's horizontal direction to make it bounce
    
        
    
    # Check for collision with the right paddle (right_paddle )
    # It checks if the ball is within the horizontal and vertical range of the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < right_paddle.ycor() + 40 and ball.ycor() > right_paddle.ycor() - 40):
        ball.setx(340)      # Move the ball to the paddle's surface to prevent it from getting stuck
        ball.dx *= -1       # Reverse the ball's horizontal direction to make it bounce