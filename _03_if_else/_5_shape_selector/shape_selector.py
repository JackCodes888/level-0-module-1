import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    jturtle = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='Which Shape', prompt='would you like to draw a circle square or triangle')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'square':
        for i in range(4):
            jturtle.forward(100)
            jturtle.right(90)
    if shape == 'circle':
        jturtle.circle(20)
    if shape == 'triangle':
        for i in range(3):
            jturtle.left(120)
            jturtle.forward(100)
    # Call the turtle .done() method
    print('done')
    turtle.done()
