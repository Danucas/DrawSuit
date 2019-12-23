#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def open_file(root, viewport, img):
    print("opening file")
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img[0] = ImageTk.PhotoImage(Image.open(filename).resize((480, 480)))
    viewport.create_image(0, 0, image=img[0], anchor="nw")
    viewport.place_forget()
    viewport.place(x=40, y=0)
    print(filename)

def save_file(root, viewport, img):
    print("saving file")
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    img[0] = ImageTk.PhotoImage(Image.open(filename).resize((480, 480)))
    viewport.create_image(0, 0, image=img[0], anchor="nw")
    viewport.place_forget()
    viewport.place(x=40, y=0)
    print(filename)

def save_as(root, viewport, img, doc):
    print("saving file as")
    filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Select File", filetypes=(("dws files", "*.dws"), ("all files", "*.*")))
    file_ac = open(filename, "w+")
    for i in doc[0]:
        if "Canvas" in doc[0][i]:
            del doc[0][i]["Canvas"]
        if "snap" in doc[0][i]:
            del doc[0][i]["snap"]
    file_ac.write("{}".format(doc[0]))
    print(filename)
