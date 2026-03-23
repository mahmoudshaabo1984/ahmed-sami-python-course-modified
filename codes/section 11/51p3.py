


# import  tkinter 
from tkinter import *


# Create the Main App Window
age_app = Tk()

# Change App title
age_app.title("Calculate Your Age")


# Set Dimensions
age_app.geometry("400x200")

# Write Age Label
the_text =Label(age_app, text="Write Your Age", height=2, font=("Arial", 20))

# Place The Text Into The Main Window
the_text.pack()


# Age Variables
age = StringVar()

# Set Default Value For Age
age.set("00")


# Create the input for age
age_input = Entry(age_app, width=2 , font=("Arial", 30), textvariable=age)


# Place the input into the main window
age_input.pack()

# Create the calculate button
button = Button(age_app, text="Calculate ", width=20, height=2, bg="#0e1063", fg="white", borderwidth=0)
# Place button in the main window
button.pack()





# Run App Infinitely
age_app.mainloop()