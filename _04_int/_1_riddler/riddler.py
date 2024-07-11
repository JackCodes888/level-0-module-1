"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import simpledialog, messagebox , Tk


window = Tk()
window.withdraw()

score = 0

question1 = simpledialog.askstring(title='Question #1',prompt='What has 6 faces no makeup and 21 eyes')

question2 = simpledialog.askstring(title='Question #2',prompt='what is easy to lift but hard to throw')

question3 = simpledialog.askstring(title='Question #3',prompt='what runs but never walks')

if question1 == 'a die':
    score += 1
if question2 == 'a feather':
    score += 1
if question3 == 'a river':
    score += 1

messagebox.showinfo(message='you got ' +str(score) + ' points')


