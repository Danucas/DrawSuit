#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def set_tools(root):
    #Tool box--------
    tool_box_cont = Frame(root)
    tool_box = Canvas(tool_box_cont, width=40, height=180)
    move_spot = Canvas(tool_box_cont, width=40, height=10, bg="black")
    move_spot.bind("<Button-1>", lambda evn: print("moving tag"))
    move_spot.pack()
    tool_1 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_1.bind("<Button-1>", lambda evn: print("tool_1"))
    tool_1.place(x=0, y=0)
    tool_2 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_2.bind("<Button-1>", lambda evn: print("tool_2"))
    tool_2.place(x=20, y=0)

    tool_3 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_3.bind("<Button-1>", lambda evn: print("tool_3"))
    tool_3.place(x=0, y=20)

    tool_4 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_4.bind("<Button-1>", lambda evn: print("tool_4"))
    tool_4.place(x=20, y=20)

    tool_5 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_5.bind("<Button-1>", lambda evn: print("tool_5"))
    tool_5.place(x=0, y=40)

    tool_6 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_6.bind("<Button-1>", lambda evn: print("tool_6"))
    tool_6.place(x=20, y=40)

    tool_7 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_7.bind("<Button-1>", lambda evn: print("tool_7"))
    tool_7.place(x=0, y=60)

    tool_8 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_8.bind("<Button-1>", lambda evn: print("tool_8"))
    tool_8.place(x=20, y=60)

    tool_9 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_9.bind("<Button-1>", lambda evn: print("tool_9"))
    tool_9.place(x=0, y=80)

    tool_10 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_10.bind("<Button-1>", lambda evn: print("tool_10"))
    tool_10.place(x=20, y=80)

    tool_11 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_11.bind("<Button-1>", lambda evn: print("tool_11"))
    tool_11.place(x=0, y=100)

    tool_12 = Canvas(tool_box, width=20, height=20, bg="green", cursor="hand1")
    tool_12.bind("<Button-1>", lambda evn: print("tool_12"))
    tool_12.place(x=20, y=100)


    tool_box.pack()
    tool_box_cont.place(x=0, y=160)
    return tool_box_cont



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



def set_layer_tools(root, layers):
    #Layer tool View
    lytool_cont = Frame(root)
    layer_tool = Canvas(lytool_cont, width=80, height=300, bg="grey")
    #Buttons container
    lb_canv = Canvas(lytool_cont, width=80, height=20, bg="brown")
    #Moving tag
    move_layer_spot = Canvas(lytool_cont, width=90, height=10, bg="black\
")
    move_layer_spot.bind("<Button-1>", lambda evn: print("moving tag"))
    move_layer_spot.pack()


    nl_icon = ImageTk.PhotoImage(Image.open(r"icons/btns/btn.png").resize((16, 16)))
    new_layer_btn = Canvas(lb_canv, width=20, height=20, bg="pink", cursor="hand2")
    new_layer_btn.bind("<Button-1>", lambda evn: print("New layer"))
    new_layer_btn.place(x=0, y=0)
    new_layer_btn.create_image(2, 2, anchor="nw", image=nl_icon)


    scroll_bar = Scrollbar(lytool_cont, orient="vertical", width=10, bg="black", command=layer_tool.yview)
    scrollable_frame = Frame(layer_tool)
    scrollable_frame.bind("<Configure>", lambda e: layer_tool.configure(scrollregion=layer_tool.bbox("all")))

    layer_tool.create_window((0, 0), window=scrollable_frame, anchor="nw")
    layer_tool.configure(yscrollcommand=scroll_bar.set)

    for item in layers.items():
        draw_layer_preview(layers, item, scrollable_frame)

    lytool_cont.place(x=520, y=0)
    lb_canv.pack(side="bottom", fill="both", expand=True)
    layer_tool.pack(side="left", fill="both", expand=True)
    scroll_bar.pack(side="right", fill="y")
    return ()

def insert_layer(layers_tool, layers, root):
    layers_tool.pack_forget()
    new_layers_tool = set_layer_tools(root, layers)
    return new_layers_tool
