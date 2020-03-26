import pyqrcode
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
url = pyqrcode.create('bad \nbad \t\t\t\t\t run\n run tuna\t bob \n rando')
url.png('uca-url.png',scale =15)
#print(url.terminal(quiet_zone=1))



root = Tk()
root.title("Feet to Meters")
root.geometry("800x900")
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#mainframe.configure(image="uca-url.svg")

load = Image.open('uca-url.png')
render = ImageTk.PhotoImage(load)
img = Label(mainframe, image=render)
img.image = render
img.place(x=0, y=0)

root.mainloop()

