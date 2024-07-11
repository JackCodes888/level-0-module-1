"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
import string
from tkinter import simpledialog, messagebox,Tk

window = Tk()
window.withdraw()

number1 = simpledialog.askinteger(title='number 1',prompt='enter a number')
number2 = simpledialog.askinteger(title='number 2', prompt='enter a number')
do = simpledialog.askstring(title='what would you like to do',prompt='tell me if you would like to add subtract multiply or divide')


if do == 'add':
    number1 += number2
if do == 'subtract':
    number1 -= number2
if do == 'multiply':
    number1 *= number2
if do == 'divide':
    number1 /= number2

messagebox.showinfo(message=number1)

