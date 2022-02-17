from fltk import *

def center_text(self, box):
    inp = box.value()
    if " " not in inp and inp != "":
        box.value("  " + inp)
    elif inp == "" or inp == " ":
        box.value("  ")
    elif len(inp) == 3 and inp[-1] == " ":
        if inp[0] != " ":
            box.value("  " + inp[0])
        elif inp[1] != " ":
            box.value("  " + inp[1])

    inp = box.value()
    digits = ["1","2","3","4","5","6","7","8","9"]
    if str(inp[-1]) not in digits:
        box.value("  ")     

