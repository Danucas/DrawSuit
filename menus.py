from tkinter import *
from file_manager import *
from cols import *
from generate_empty_pattern import *

def set_menubar(root, viewport, doc):
    #File Menu
    cols = getColors()
    menubar = Menu(root, bg=cols["grey_cont"], fg="white")
    image = [None]
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="{}".format("Open"), command=lambda : open_file(root, viewport, image, doc))
    filemenu.add_command(label="{}".format("Save"), command=lambda: save_file(root, viewport, image))
    filemenu.add_command(label="Save as", command=lambda: save_as(root, viewport, image, doc))
    filemenu.add_command(label="Quit", command=root.quit)
    filemenu.add_command(label="Generate Empty", command=lambda: draw_empty(viewport))
    filemenu.add_command(label="Print colors", command=lambda: print_colors(root))
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)
    return menubar
