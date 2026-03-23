



# import  tkinter 
from tkinter import * # Import all classes and functions from the tkinter library
# import messagebox
from tkinter import messagebox # Imports the messagebox module for pop-up windows.

# Create the Main App Window
window = Tk() # Create the main application window.

# Change App Text
window.title("Calculate Your Age")  # Set the title of the window.

# Set Dimensions
window.geometry("400x200") # Sets the dimensions of the window (width x height).

# Write Age Label
the_text = Label(window, text="Write Your Age", height=2, font=("Arial" , 20)) # Creates a text label widget.

# Place The Text Into The Main Window
the_text.pack() # Places the label widget into the main window.


# Age Variables
age =StringVar() # Creates a special tkinter variable to hold a string.


# Set Default Value For Age
age.set("00") # Sets the default value for the 'age' variable.


# Create the input for age
age_input = Entry(window, width=2, font=("Arial", 30), textvariable=age)  # Creates an input field for the user to type their age.

# Place the input into the main window
age_input.pack() # Adds the input field to the window.

# Create the calculate function
def calc(): # Defines a function to perform the age calculation when called.
    # Get Age In Years and convert to an integer
    the_age_value = int(age.get()) # Retrieves the value from the `age` variable and converts it to an integer.

    # Get Time Units
    months = the_age_value * 12 # Calculates the number of months.
    weeks = months * 4 # Calculates the number of weeks.
    days = the_age_value * 365# Calculates the number of days.

    # Create Text Lines
    line_one = f"Your Age In Months Is: {months}" # Formats a string to display age in months.
    line_two = f"Your Age In Weeks Is: {weeks}" # Formats a string to display age in weeks.
    line_three = f"Your Age In Days Is: {days}" # Formats a string to display age in days.
    
    

    # Group all lines
    all_lines = [line_one, line_two, line_three] # Combines all lines into a list.
    
    
    # Show The Message Box
    # Displays a pop-up box with the calculated age details.
    messagebox.showinfo("Your Age In All Time Units", "\n".join(all_lines)) 
    



# Create the calculate button
# Creates a button with custom text and colors.
button = Button(window, text="Calculate", width=20, height=2, bg="#0e1063", fg="white", borderwidth=0, command=calc)

# Place button in the main window
button.pack() # Adds the button to the window.






# Run App Infinitely
window.mainloop() # Run the application's event loop to keep it open.
