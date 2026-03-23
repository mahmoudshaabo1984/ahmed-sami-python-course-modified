



# Import the turtle module, which provides graphics and drawing capabilities in Python
import turtle

# Create a window (screen) object using turtle.Screen() to set up the game environment
wind = turtle.Screen()

# Set the title of the window to "Ping Pong By Codezilla"
wind.title("Ping Pong By Codezilla")

# Set the background color of the window to black
wind.bgcolor("black")

# Set up the dimensions of the window: width=800 pixels, height=600 pixels
wind.setup(width=800, height=600)

# Disable automatic screen updates (tracer(0) means updates must be manual for better performance in games)
wind.tracer(0)

# madrab1
madrab1 = turtle.Turtle()  # Create a turtle object for paddle 1
madrab1.speed(0)  # Set the animation speed to maximum (0 = fastest)
madrab1.shape("square")  # Set the shape to square
madrab1.color("blue")  # Set the color to blue
madrab1.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square vertically by 5 and horizontally by 1
madrab1.penup()  # Lift the pen up to prevent drawing lines when moving
madrab1.goto(-350, 0)  # Position the paddle at x=-350, y=0

# madrab2
madrab2 = turtle.Turtle()  # Create a turtle object for paddle 2
madrab2.speed(0)  # Set the animation speed to maximum (0 = fastest)
madrab2.shape("square")  # Set the shape to square
madrab2.color("red")  # Set the color to red
madrab2.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the square vertically by 5 and horizontally by 1
madrab2.penup()  # Lift the pen up to prevent drawing lines when moving
madrab2.goto(350, 0)  # Position the paddle at x=350, y=0

# ball
ball = turtle.Turtle()  # Create a turtle object for the ball
ball.speed(0)  # Set the animation speed to maximum (0 = fastest)
ball.shape("square")  # Set the shape to square
ball.color("white")  # Set the color to white
ball.penup()  # Lift the pen up to prevent drawing lines when moving
ball.goto(0, 0)  # Position the ball at the center (x=0, y=0)

# functions
def madrab1_up():  # Define function to move paddle 1 up
    y = madrab1.ycor()  # Get the current y coordinate of paddle 1
    y += 20  # Increase y by 20
    madrab1.sety(y)  # Set the new y coordinate

def madrab1_down():  # Define function to move paddle 1 down
    y = madrab1.ycor()  # Get the current y coordinate of paddle 1
    y -= 20  # Decrease y by 20
    madrab1.sety(y)  # Set the new y coordinate

def madrab2_up():  # Define function to move paddle 2 up
    y = madrab2.ycor()  # Get the current y coordinate of paddle 2
    y += 20  # Increase y by 20
    madrab2.sety(y)  # Set the new y coordinate

def madrab2_down():  # Define function to move paddle 2 down
    y = madrab2.ycor()  # Get the current y coordinate of paddle 2
    y -= 20  # Decrease y by 20
    madrab2.sety(y)  # Set the new y coordinate

# keyboard bindings
wind.listen()  # Tell the window to listen for keyboard input
wind.onkeypress(madrab1_up, "w")  # When 'w' key is pressed, call madrab1_up function
wind.onkeypress(madrab1_down, "s")  # When 's' key is pressed, call madrab1_down function
wind.onkeypress(madrab2_up, "Up")  # When 'Up' arrow key is pressed, call madrab2_up function
wind.onkeypress(madrab2_down, "Down")  # When 'Down' arrow key is pressed, call madrab2_down function

# main game loop
while True:  # Start an infinite loop to keep the game running
    wind.update()  # Update the screen to reflect any changes (since tracer is off)