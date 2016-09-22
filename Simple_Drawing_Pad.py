from tkinter import *
from tkinter import ttk        
    
root = Tk()

def mouse_press(event):
    global prev
    prev = event
    print('type: {}'.format(event.type))
    print('widget: {}'.format(event.widget))
    print('num: {}'.format(event.num))
    print('x: {}'.format(event.x))
    print('y: {}'.format(event.y))
    print('x: {}'.format(event.x_root))
    print('y: {}'.format(event.y_root))


canvas = Canvas(root, width = 640, height = 480, background = 'white')
canvas.pack()

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y, width = 5)
    prev = event
   

canvas.bind('<ButtonPress>', mouse_press)
canvas.bind('<B1-Motion>', draw)

root.mainloop()
