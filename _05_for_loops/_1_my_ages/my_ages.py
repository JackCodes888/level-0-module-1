from tkinter import simpledialog,messagebox,Tk
window = Tk()
window.withdraw()


for i in range(11):
    messagebox.showinfo(message= 'I have been ' + str(i + 1))
