#!/usr/bin/python3
from cols import *
from tkinter import *
#Creating new pencil
def get_pencil():
    colors = getColors()
    pencil = {}
    pencil["shape"] = "elipse"
    pencil["width"] = 8
    pencil["color"] = colors["brush"]
    return pencil

def pencil_draw(evn, viewport):
    pencil = get_pencil()
    if pencil["shape"] == "elipse":
        x1 = int(evn.x - (pencil["width"] / 2))
        y1 = int(evn.y - (pencil["width"] / 2))
        x2 = int(evn.x + (pencil["width"] / 2))
        y2 = int(evn.y + (pencil["width"] / 2))
        viewport.create_oval(x1, y1, x2, y2, fill=pencil["color"] )