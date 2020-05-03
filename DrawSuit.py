#!/usr/bin/python3
from tkinter import *
from utilities.file_manager import *
from api.v1.views.tools import *
from api.v1.views.tool_bar import *
from api.v1.views.viewport import *
from api.v1.views.menus import *
from utilities.cols import *
from PIL import Image, ImageTk

root = Tk()
cols = getColors()
win_dim = {"width": root.winfo_screenwidth() - 400, "height": root.winfo_screenheight() - 3}
root.geometry("{}x{}+400+0".format(win_dim["width"], win_dim["height"]))
root.configure(background=cols["background"])
root.title("DrawSuit")


def hello():
    print("Hello");



#-----------------------------
#Setting UI
actual_tool = ["rect_selection"]
viewport , dim = set_viewport(root, actual_tool)
layers = {"layer_01": {"image": "icons/btns/gree.png"}, "layer_02": {"drawable": {"type": "rect", "ini":{"x": 10, "y": 10}, "fin": {"x": 100, "y": 100}, "bg": "#ffbbaa"}}}
doc = [layers]
lytool = set_layer_tools(root, layers)
tools, actual_tool = set_tools(root, actual_tool)
tool_bar = set_tool_bar(root)
menubar = set_menubar(root, viewport, doc)


root.mainloop()
