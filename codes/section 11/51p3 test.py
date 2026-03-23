



# import  tkinter 
from tkinter import * # Imports everything from the Tkinter library.


# Create the Main App Window
age_app = Tk() # Creates the main application window.

# Change App title
age_app.title("Calculate Your Age") # Sets the title of the window.


# Set Dimensions
age_app.geometry("400x200") # Sets the width and height of the window.

# Write Age Label
the_text =Label(age_app, text="Write Your Age", height=2, font=("Arial", 20)) # Creates a label with text.

# Place The Text Into The Main Window
the_text.pack() # Adds the label to the window.


# Age Variables
age = StringVar() # Creates a variable to store the age as a string.

# Set Default Value For Age
age.set("00") # Sets the default value of the age variable to "00".


# Create the input for age
age_input = Entry(age_app, width=2 , font=("Arial", 30), textvariable=age) # Creates an input field for the user to type their age.


# Place the input into the main window
age_input.pack() # Adds the input field to the window.

# Create the calculate button
button = Button(age_app, text="Calculate ", width=20, height=2, bg="#0e1063", fg="white", borderwidth=0) # Creates a button with custom text and colors.
# Place button in the main window
button.pack() # Adds the button to the window.





# Run App Infinitely
age_app.mainloop() # Starts the Tkinter event loop, which runs the application.