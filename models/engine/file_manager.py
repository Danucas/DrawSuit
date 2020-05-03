#!/usr/bin/python3
"""
Handle the file reading logic
"""
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import json
import os


def open_file(root, viewport, img, doc):
    """
    Prompt the file picker to select the path to be open
    """
    print("opening file")
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("png files", "*.png"), ("dws files", "*.dws"), ("all files", "*.*")))
    print(filename[-3:])
    print(filename)
    if filename[-3:] == "dws":
        file_n = open(filename,"r")
        content = json.loads(file_n.read())
        file_n.close()
        print(content)
        doc[0] = content
    else:
        print("Open imagefile")
        img[0] = ImageTk.PhotoImage(Image.open(filename).resize((600, 600)))
        viewport.create_image(0, 0, image=img[0], anchor="nw")

def save_file(root, viewport, img):
    """
    Save all frames combined from actual workplace
    require:
        handle different file formats
    """
    print("saving file")
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img[0] = ImageTk.PhotoImage(Image.open(filename).resize((480, 480)))
    viewport.create_image(0, 0, image=img[0], anchor="nw")
    viewport.place_forget()
    viewport.place(x=40, y=0)
    print(filename)

def save_as(root, viewport, img, doc):
    """
    Serialize and save json representation for all frames and states
    required:
        handle new objects
    """
    print("saving file as")
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("dws files", "*.dws"), ("all files", "*.*")))
    file_ac = open(filename, "w+")
    for i in doc[0]:
        if "Canvas" in doc[0][i]:
            del doc[0][i]["Canvas"]
        if "snap" in doc[0][i]:
            del doc[0][i]["snap"]
    file_ac.write(json.dumps(doc[0], indent=4, sort_keys=True))
    file_ac.close()
    print(filename)
