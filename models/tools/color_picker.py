#!/usr/bin/python3
import tkinter as tk

def color_picker(root):
    ranges = []
    ranges.append([255, {"r":255, "g":0, "b":0}])
    ranges.append([510, {"r":255, "g":255, "b":0}])
    ranges.append([765, {"r":0, "g":255, "b":0}])
    ranges.append([1020, {"r":0, "g":255, "b":255}])
    ranges.append([1275, {"r":0, "g":0, "b":255}])
    ranges.append([1530, {"r":255, "g":0, "b":255}])


    actualRange = [0]
    actualRGB = [{"r": 255,"g": 0, "b": 0}]
    width = 200
    height = 100
    x, y = 0, 0

    picker_cont = tk.Canvas(root, width=600, height=300, bg="grey")
    palette = tk.Canvas(picker_cont, width=400, height=200, bg="white", cursor="cross")
    sample = tk.Canvas(picker_cont, width=200, height = 200)
    sample.place(x=0, y=0)

    palette.place(x=200, y=0)

    """Setting, an scroll bar for the saturation"""

    sat_bar = tk.Canvas(picker_cont, width=480, height=26, bg="grey", cursor="hand2")
    scroll_line = sat_bar.create_rectangle(3, 10, 474, 16, fill="white")

    """Draw the saturation map in the scroller"""

    sat_map = []
    def draw_satline():
        w = 471
        for x in range(1, w):
            x_percent = (x * 100) / w
            pos = int((1530 * x_percent) / 100)
            last = 0
            p = 0
            for i, rango in enumerate(ranges):
                if pos <= rango[0] and pos > last:
                    p = i
                    break;
                last = rango[0]
            col = {}
            if p == 0:
                diff = pos - last
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": ranges[p][1]["r"], "g": int(255 * dif_percent), "b": ranges[p][1]["b"]}
            if p == 1:
                diff = 255 - (pos - last)
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": int(255 * dif_percent), "g": ranges[p][1]["g"], "b": ranges[p][1]["b"]}
            if p == 2:
                diff = (pos - last)
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": ranges[p][1]["r"], "g": ranges[p][1]["g"], "b": int(255 * dif_percent)}
            if p == 3:
                diff = 255 - (pos - last)
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": ranges[p][1]["r"], "g": int(255 * dif_percent), "b": ranges[p][1]["b"]}
            if p == 4:
                diff = (pos - last)
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": int(255 * dif_percent), "g": ranges[p][1]["g"], "b": ranges[p][1]["b"]}
            if p == 5:
                diff = 255 - (pos - last)
                dif_percent = (diff * (100 / 255)) / 100
                col = {"r": ranges[p][1]["r"], "g": ranges[p][1]["g"], "b": int(255 * dif_percent)}
            if "r" in col:
                new_c = "#{:0>2x}{:0>2x}{:0>2x}".format(col["r"], col["g"], col["b"])
                sat_bar.create_line(3 + x, 10, 3 + x, 16, fill=new_c)
                sat_map.append(col)
    draw_satline()
    Wd = 400
    Hg = 200


    """Printing the palette gradient"""
    def get_gradient():
        picker_cont.config(cursor="watch")
        root.config(cursor="watch")
        new_col = {"r": 0,"g": 0, "b": 0}
        pixels = [None for i in range(Wd * Hg)]
        for x in reversed(range(Wd)):
            for y in range(Hg):
                x_percent = ((100 - ((x * 100) / Wd)) / 100)
                y_percent = ((100 - ((y * 100) / Hg)) / 100)
                for col in actualRGB[0]:
                    if ranges[actualRange[0]][1][col] == 255:
                        new_col[col] = (actualRGB[0][col] * y_percent)
                    elif actualRGB[0][col] == 0:
                        new_col[col] = (255 * x_percent) * y_percent
                    elif actualRGB[0][col] > 0:
                        new_col[col] = (actualRGB[0][col] * x_percent) * y_percent
                    r, g, b = int(new_col["r"]), int(new_col["g"]), int(new_col["b"])
                    hexCol = "#{:0>2x}{:0>2x}{:0>2x}".format(r, g, b)
                    pixels[(Wd * y) + x] = hexCol
                    palette.create_rectangle(x, y, x, y, fill=hexCol, outline=hexCol)
        picker_cont.config(cursor="")
        root.config(cursor="")
        return pixels

    """Drawing a circle in the selected color"""

    sel_oval = [None]
    pixls = get_gradient()
    def selectColor(evn):
        print("selected color: {}".format(pixls[(Wd * evn.y) + evn.x]))
        sample.config(background=pixls[(Wd * evn.y) + evn.x])
        if sel_oval[0] != None:
            palette.delete(sel_oval[0])
        sel_oval[0] = palette.create_oval(evn.x - 13, evn.y - 13, evn.x + 13, evn.y + 13, stipple="gray12") 

    palette.bind("<Button-1>", lambda evn: selectColor(evn))

    """Setting  the saturation picker behavior"""

    selector = sat_bar.create_oval(1, 1, 25, 25, fill="white")
    sel_pick = [False]
    last = [0]
    def move_selector(evn):
        if sel_pick[0] is True:
            new_p = evn.x - 13
            if evn.x > 13 and evn.x < 467:
                diff = (int(new_p)) - last[0]
                sat_bar.move(selector, diff, 0)
                last[0] = evn.x - 13
    def sel_on():
        sel_pick[0] = True
    def sel_off(evn):
        w = 471
        x_percent = (evn.x * 100) / w
        pos = int((1530 * x_percent) / 100)
        last = 0
        p = 0
        for i, rango in enumerate(ranges):
            if pos <= rango[0] and pos > last:
                p = i
                break;
            last = rango[0]
        actualRange[0] = p
        actualRGB[0] = sat_map[evn.x]
        print("Getting gradient")
        pixls = get_gradient()
        print("Gradient setted rgb: {}, range actual: {}".format(actualRGB[0], actualRange))
        move_selector(evn)
        sel_pick[0] = False

    sat_bar.bind("<Button-1>", lambda evn: sel_on())
    sat_bar.bind("<ButtonRelease-1>", lambda evn: sel_off(evn))
    sat_bar.bind("<Motion>", lambda evn: move_selector(evn))
    sat_bar.place(x=20, y=260)
    picker_cont.place(x=200, y=200)
