#!/usr/bin/python3
from pencil import *
from PIL import Image, ImageDraw
def tool_selector(draw_img, evn, ini, fin, sel, actual, ar, viewport, state):
    if actual[0] == "pencil":
        if state == 0:
            sel[0] = True
            ini[0] = evn.x
            ini[1] = evn.y
            fin[0] = evn.x
            fin[1] = evn.y
            pencil_draw(evn, viewport, (None))
        if state == 1 and sel[0] is True:
            ini[0] = fin[0]
            ini[1] = fin[1]
            fin[0] = evn.x
            fin[1] = evn.y
            pencil_draw(evn, viewport, (ini, fin))
        if state == 2:
            sel[0] = False
    elif actual[0] == "rect_selection":
        print("rect_selection")
        if state == 1 and sel[0] == True:
            if ar[0] != None:
                viewport.delete(ar[0])
                fin[0] = evn.x
                fin[1] = evn.y
                ar[0] = viewport.create_rectangle(ini[0], ini[1], fin[0], fin[1], outline="#000000", fill="#FFFFFF", dash=(4, 2), stipple="gray12")
            
        elif state == 0:
            ini[0] = evn.x
            ini[1] = evn.y
            sel[0] = True
        elif state == 2:
            viewport.delete(ar[0])
            fin[0] = evn.x
            fin[1] = evn.y
            sel[0] = False
            ar[0] = viewport.create_rectangle(ini[0], ini[1], fin[0], fin[1], outline="#000000",    fill="#FFFFFF", dash=(4, 2), stipple="gray12")
            print("rectangle object")
            for fun in viewport.find_withtag(ar[0]):
                print(viewport.type(fun))
            draw_img[0].rectangle([ini[0], ini[1], fin[0], fin[1]], fill="#000000")
            draw_img[1].save("rect_test.png", 'PNG')
