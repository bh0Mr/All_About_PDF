import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Dark background for better contrast
screen.title("Oddly Satisfying Infinite Circle Loop")

# Create a turtle
t = turtle.Turtle()
t.shape("turtle")
t.speed(0)  # Fastest drawing speed
t.width(2)  # Set the pen width for a smoother circle

# Function to change the color of the turtle's pen
def random_color():
    return random.choice(["red", "green", "blue", "purple", "orange", "yellow", "pink", "cyan"])

# Infinite loop to draw circles in an oddly satisfying way
while True:
    t.color(random_color())  # Change color for each circle
    t.circle(100)  # Draw a circle with radius 100
    t.left(5)  # Smoothly rotate the turtle
    t.penup()   # Lift pen to avoid continuous lines
    t.goto(t.xcor() + 2, t.ycor() + 2)  # Slightly offset the position to create a new track
    t.pendown()  # Put pen back down for next circle
