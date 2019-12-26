#!/usr/bin/python3
from tkinter import *
from PIL import Image, ImageDraw
from cols import getColors

def draw_empty(viewport):
    image = Image.new("RGBA", (600, 600), (255, 255, 255, 0))
    colrs = getColors()
    draw = ImageDraw.Draw(image)
    bw = 6
    width = (viewport.winfo_width() / bw) + 1
    height = (viewport.winfo_height() / bw) + 1
    for y in range(1, int(height)):
        for x in range(1, int(width)):
#            print(x, y)
            if (y % 2) != 0:
                print("y is odd")
                if (x % 2) != 0:
                    print(" x is odd")
                    draw.rectangle([(x - 1) * bw, (y - 1) * bw, ((x - 1) * bw) + bw, ((y - 1) * bw) + bw], fill=colrs["empty"])
            else:
                print("y is even")
                if x % 2 == 0:
                    draw.rectangle([(x - 1) * bw, (y - 1) * bw, ((x - 1) * bw) + bw, ((y - 1) * bw) + bw], fill=colrs["empty"])
    print(viewport.winfo_width(), viewport.winfo_height())
    image.save("empty_pattern.png", 'PNG')
