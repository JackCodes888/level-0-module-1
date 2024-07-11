"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user

"""
from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()


number1 = simpledialog.askinteger(title='',prompt='please enter a number')
number2 = simpledialog.askinteger(title='',prompt='please enter a number' )

number2 += number1
str(number2)
messagebox.showinfo(message= number2)
