#!/usr/bin/python3
from cols import *
from tkinter import *
#Creating new pencil
def get_pencil():
    colors = getColors()
    pencil = {}
    pencil["shape"] = "elipse"
    pencil["width"] = 2
    pencil["color"] = colors["brush"]
    return pencil

def pencil_draw(evn, viewport, coords):
    pencil = get_pencil()
    if pencil["shape"] == "elipse":
        if coords is not None:
            coords = list(coords)
            if coords[0][0] > coords[1][0]:
                coords[0], coords[1] = coords[1], coords[0]
            if coords[0][1] > coords[1][1]:
                coords[0], coords[1] = coords[1], coords[0]
            diffx = coords[1][0] - coords[0][0]
            diffy = coords[1][1] - coords[0][1]
            if diffx == 0:
                diffx = 1
            if diffy == 0:
                diffy = 1
            if diffy > diffx:
                part = diffx / diffy
                x = coords[0][0]
                for y in range(coords[0][1], coords[1][1]):
                    x = x + part
                    x1 = int(x - (pencil["width"] / 2))
                    y1 = int(y - (pencil["width"] / 2))
                    x2 = int(x + (pencil["width"] / 2))
                    y2 = int(y + (pencil["width"] / 2))
                    viewport.create_oval(x1, y1, x2, y2, fill=pencil["color"] )
            else:
                part = diffy / diffx
                y = coords[0][1]
                for x in range(coords[0][0], coords[1][0]):
                    y = y + part
                    x1 = int(x - (pencil["width"] / 2))
                    y1 = int(y - (pencil["width"] / 2))
                    x2 = int(x + (pencil["width"] / 2))
                    y2 = int(y + (pencil["width"] / 2))
                    viewport.create_oval(x1, y1, x2, y2, fill=pencil["color"] )
        else:
            x1 = int(evn.x - (pencil["width"] / 2))
            y1 = int(evn.y - (pencil["width"] / 2))
            x2 = int(evn.x + (pencil["width"] / 2))
            y2 = int(evn.y + (pencil["width"] / 2))
            viewport.create_oval(x1, y1, x2, y2, fill=pencil["color"] )
