from tkinter import *

window_width = 800
window_height = 800
root = Tk()

canvas = Canvas(root, width=window_width, height=window_height, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()


# This code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # Draws a dark blue background
    canvas.create_rectangle(0, 0, window_width, window_height, fill="#000050")

    # x and y will be equal to the mouse pointer's x and y location
    x = event.x
    y = event.y

    points_circle = [x + 100, y, x - 100  , y + 100]
    # This defines the x and y coordinated of all three points
    # of a triangle
    points = [x + 50, y, x - 50, y , x , y - 50]
    canvas.create_polygon(points, fill='gray', width=2) # draws triangle
    canvas.create_oval(points_circle, fill='red', width=3)
    # 1. Add details to your rocket to make it look better. You can look at
    #    rocket.png for inspiration.
    
    # 2. Modify the locations of the shapes above so the rocket will be drawn
    #    where the mouse is clicked
    

# ====================== DO NOT MODIFY THE CODE BELOW ========================

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()
