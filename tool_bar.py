#!/usr/bin/py
from tkinter import *
from cols import *

def set_tool_bar(root):
    colores = getColors()
    cont = Frame(root, width=root.winfo_screenwidth() - 3, height=30, bg=colores["grey_cont"]).pack()
