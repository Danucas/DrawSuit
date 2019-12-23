#!/usr/bin/python3
from tkinter import *
from file_manager import *
from tools import *
from viewport import *
from menus import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("615x480")
root.title("DrawSuit")


def hello():
    print("Hello");



#-----------------------------
#Setting UI
viewport , dim = set_viewport(root)
layers = {"layer_1": {"image": "/home/dan/python/DrawSuit/icons/btns/gree.png"}, "layer_2": {"drawable": {"type": "rect", "ini":{"x": 10, "y": 10}, "fin": {"x": 100, "y": 100}, "bg": "#ffbbaa"}}}
doc = [layers]
lytool = set_layer_tools(root, layers)
tools = set_tools(root)
menubar = set_menubar(root, viewport, doc)


root.mainloop()
