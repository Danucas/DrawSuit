#!/usr/bin/python3
from tkinter import *

def getColors():
    colors = {}
    colors["background"] = "#2a2e30"
    colors["grey_cont"] = "#4d5357"
    colors["grey_1"] = "#656a6e"
    colors["empty"] = "#bdbbbb"
    colors["brush"] = "#000000"
    return colors

def print_colors(root):
    cols = getColors()
    window = Frame(root)
    for key in cols:
        t = Text(window, bg=cols[key], fg="white", height=1, width=30)
        t.insert(END, "{:<18} {:>8}".format(key, cols[key]))
        t.pack()
    window.place(x=50, y=50)
