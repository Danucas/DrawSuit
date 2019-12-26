#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os


def set_actual_tool(actual_tool, tool):
    print("actual tool {}".format(tool))
    actual_tool[0] = tool

def set_tools(root, actual_tool):
    #Tool box--------
    tool_box_cont = Frame(root)
    tag = ["tag"]
    tool_box = Canvas(tool_box_cont, width=30, height=root.winfo_screenheight()-30)
    move_spot = Canvas(tool_box_cont, width=30, height=10, bg="black")
    move_spot.bind("<Button-1>", lambda evn: print("moving tag"))
    move_spot.pack()
    tool_1 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_1.bind("<Button-1>", lambda evn: print("tool_1"))
    tool_1.place(x=0, y=0)
    tool_2 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_2.bind("<Button-1>", lambda evn: print("tool_2"))
    tool_2.place(x=0, y=30)

    tool_3 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_3.bind("<Button-1>", lambda evn: print("tool_3"))
    tool_3.place(x=0, y=60)

    tool_4 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_4.bind("<Button-1>", lambda evn: print("tool_4"))
    tool_4.place(x=0, y=90)

    tool_5 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_5.bind("<Button-1>", lambda evn: print("tool_5"))
    tool_5.place(x=0, y=120)
    def print_tool_tag(evn, txt, y):
        tag[0] = Text(root, width=len(txt), height=1)
        tag[0].insert(END, txt)
        tag[0].place(x=evn.x, y=y)
    def remove_tag():
        tag[0].place_forget()
#   pencil
    tool_6 = Canvas(tool_box, width=30, height=30, bg="red", cursor="hand2")
    tool_6.bind("<Button-1>", lambda evn: set_actual_tool(actual_tool, "pencil"))
    tool_6.bind("<Leave>", lambda x: remove_tag())
    tool_6.bind("<Enter>", lambda evn: print_tool_tag(evn, "Pencil", 140 + 60))
    tool_6.place(x=0, y=150)

    tool_7 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_7.bind("<Button-1>", lambda evn: print("tool_7"))
    tool_7.place(x=0, y=180)

    tool_8 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_8.bind("<Button-1>", lambda evn: print("tool_8"))
    tool_8.place(x=0, y=210)

    tool_9 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_9.bind("<Button-1>", lambda evn: print("tool_9"))
    tool_9.place(x=0, y=240)

    tool_10 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_10.bind("<Button-1>", lambda evn: print("tool_10"))
    tool_10.place(x=0, y=270)

    tool_11 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_11.bind("<Button-1>", lambda evn: print("tool_11"))
    tool_11.place(x=0, y=300)

    tool_12 = Canvas(tool_box, width=30, height=30, bg="green", cursor="hand2")
    tool_12.bind("<Button-1>", lambda evn: print("tool_12"))
    tool_12.place(x=0, y=330)


    tool_box.pack()
    tool_box_cont.place(x=0, y=30)
    return tool_box_cont, actual_tool



def draw_layer_preview(layers, layer, frame):
    layer = layers[layer[0]]
    canvas = Canvas(frame, width=80, height=50, bg="blue", cursor="hand1")
    canvas.pack()
    layer["Canvas"] = canvas
    if "image" in layer:
        print(layer["image"])
        layer["snap"] = ImageTk.PhotoImage(Image.open(layer["image"]).resize((80, 50)))
        canvas.create_image(0, 0, image=layer["snap"], anchor="nw")
    if "drawable" in layer:
        print(layer["drawable"])

def insert_layer(layers_tool, layers, root):
    layers_tool.pack_forget()
    indx = len(layers.items())
    dic = "layer_{:0>2d}".format(indx + 1)
    print(dic)
    layers[dic] = {"bg": "red"}
    new_layers_tool = set_layer_tools(root, layers)
    return new_layers_tool

def set_layer_tools(root, layers):
    #Layer tool View
    lytool_cont = Frame(root)
    layer_tool = Canvas(lytool_cont, width=390, height=root.winfo_screenheight()-30, bg="grey")
    #Buttons container
    lb_canv = Canvas(lytool_cont, width=390, height=30, bg="brown")
    #Moving tag
    move_layer_spot = Canvas(lytool_cont, width=400, height=10, bg="black\
")
    move_layer_spot.bind("<Button-1>", lambda evn: print("moving tag"))
    move_layer_spot.pack()


    nl_icon = ImageTk.PhotoImage(Image.open(r"icons/btns/btn.png").resize((16, 16)))
    new_layer_btn = Canvas(lb_canv, width=30, height=30, bg="pink", cursor="hand2")
    new_layer_btn.bind("<Button-1>", lambda evn: insert_layer(lytool_cont, layers, root))
    new_layer_btn.place(x=0, y=0)
    new_layer_btn.create_image(2, 2, anchor="nw", image=nl_icon)


    scroll_bar = Scrollbar(lytool_cont, orient="vertical", width=10, bg="black", command=layer_tool.yview)
    scrollable_frame = Frame(layer_tool)
    scrollable_frame.bind("<Configure>", lambda e: layer_tool.configure(scrollregion=layer_tool.bbox("all")))

    layer_tool.create_window((0, 0), window=scrollable_frame, anchor="nw")
    layer_tool.configure(yscrollcommand=scroll_bar.set)

    for item in layers.items():
        draw_layer_preview(layers, item, scrollable_frame)

    lytool_cont.place(x=root.winfo_screenwidth() - 400, y=30)
    lb_canv.pack(side="bottom", fill="both", expand=True)
    layer_tool.pack(side="left", fill="both", expand=True)
    scroll_bar.pack(side="right", fill="y")
    return lytool_cont
