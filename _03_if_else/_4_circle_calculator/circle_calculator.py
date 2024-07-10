# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr


import math
from tkinter import simpledialog, messagebox, Tk
import turtle


window = Tk()
raduis =simpledialog.askinteger(title='Raduis',prompt='Enter youur raduis')

Question = simpledialog.askstring(title='would you like the area or cicumfrence',prompt='enter either one here')

area = math.pi * (raduis * raduis)
circumfrence = math.pi * 2 *raduis
if Question == 'circumfrence':
    print(circumfrence)

if Question == 'area':
    print(area)
