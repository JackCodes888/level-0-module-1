import turtle
from tkinter import messagebox, simpledialog, Tk

window = Tk()
birthday = simpledialog.askstring(title='',prompt='Enter your month and day of your birthday')

if birthday == "7/10":
    messagebox.showinfo(message='Happy Birthday')
else:
    messagebox.showinfo(message='Happy Unbirthday')
