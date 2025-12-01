from tkinter import *

window = None
canvas = None
XSIZE, YSIZE = 256, 256

window = Tk()

canvas = Canvas(window, hegiht = XSIZE, width = YSIZE)

canvas.pack()

window.mainloop()
