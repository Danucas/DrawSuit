from tkinter import *

def set_viewport(root):
    #Adding viewport
    #viewport dimensions
    doc_dim = {"width": 480, "height": 480}
    viewport = Canvas(root, cursor="crosshair", width=doc_dim["width"], height=doc_dim["height"], bg="#cfcbc2")
    initial = [0, 0]
    final = [0, 0]
    selecting = [False]
    area = [None]
    #viewport cursor event handler

    def click(event, ini, sel):
        print("\033[92m{}, {}\033[0m".format(event.x, event.y))
        ini[0] = event.x
        ini[1] = event.y
        sel[0] = True
        print(ini)

    def motion(event, ini, fin, sel, ar):
        if sel[0] is True:
            if ar[0] != None:
                viewport.delete(ar[0])
                fin[0] = event.x
                fin[1] = event.y
                ar[0] = viewport.create_rectangle(ini[0], ini[1], fin[0], fin[1], outline="#000000", fill="#FFFFFF", dash=(4, 2), stipple="gray12")

    def release(event, ini, fin, sel, ar):
        print("\033[91m{}, {}\033[0m".format(event.x, event.y))
        print(ini)
        viewport.delete(ar[0])
        fin[0] = event.x
        fin[1] = event.y
        sel[0] = False
        ar[0] = viewport.create_rectangle(ini[0], ini[1], fin[0], fin[1], outline="#000000", fill="#FFFFFF", dash=(4, 2), stipple="gray12")

    # -----------------------------------
    # Tool options menu like Cut copy

    def copy_area(ini, fin):
        print("Copy area")
        if ini[0] == 0 and fin[0] == 0:
            print("Seleted area is empty")
        print("from {} to {}".format(ini, fin))
        fin[0] = 0
        fin[1] = 0
        ini[0] = 0
        ini[1] = 0

    def cut_area(ini, fin):
        print("Cut area")
        print("from {} to {}".format(ini, fin))
        if ini[0] == 0 and fin[0] == 0:
            print("Seleted area is empty")
        fin[0] = 0
        fin[1] = 0
        ini[0] = 0
        ini[1] = 0

    def cut_and_copy(ini, fin):
        print("Cut and Copy")
        print("from {} to {}".format(ini, fin))
        if ini[0] == 0 and fin[0] == 0:
            print("Seleted area is empty")
        fin[0] = 0
        fin[1] = 0
        ini[0] = 0
        ini[1] = 0

    tool_opt = Menu(root, tearoff=0)
    tool_opt.add_command(label="Copy", command=lambda: copy_area(initial, finalx))
    tool_opt.add_command(label="Cut", command=lambda: cut_area(initial, final))
    tool_opt.add_command(label="Cut & Copy", command=lambda: cut_and_copy(initial, final))

    def show_tool_options(event):
        try:
            tool_opt.tk_popup(event.x_root, event.y_root)
        finally:
            tool_opt.grab_release()
    #------------------------------------
    #binding cursor events

    viewport.bind('<Button-1>', lambda evn: click(evn, initial, selecting))
    viewport.bind('<Motion>', lambda evn: motion(evn, initial, final, selecting, area))
    viewport.bind('<ButtonRelease-1>', lambda evn: release(evn, initial, final, selecting, area))
    viewport.bind('<Button-3>', lambda evn: show_tool_options(evn))
    viewport.bind('<Control-Key-s>', lambda evn: print("control-s pressed"))
    viewport.place(x=40, y=0)
    return (viewport, doc_dim)