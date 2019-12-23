from tkinter import *
from file_manager import *

def set_menubar(root, viewport, doc):
    #File Menu
    menubar = Menu(root)
    image = [None]
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=lambda : open_file(root, viewport, image))
    filemenu.add_command(label="Save", command=lambda: save_file(root, viewport, image))
    filemenu.add_command(label="Save as", command=lambda: save_as(root, viewport, image, doc))
    filemenu.add_command(label="Quit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    return menubar
