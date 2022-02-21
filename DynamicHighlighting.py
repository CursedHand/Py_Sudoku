from fltk import *

def getcurrentgrid(self, current_selection):
    if current_selection[0] <= 2:  #left
        if current_selection[1] <= 2:  #Top left
            return 0
        elif current_selection[1] <= 5:    #Middle left
            return 3
        else:                                   #Bottom Left
            return 6
    elif current_selection[0] <= 5:    #center
        if current_selection[1] <= 2:      #Top center
            return 1
        elif current_selection[1] <= 5:    #Middle center
            return 4
        else:                                   #Bottom center
            return 7
    else:                       #Right
        if current_selection[1] <= 2:      #Top Right
            return 2
        elif current_selection[1] <= 5:       #Middle right
            return 5
        else:                                   #Bottom Right
            return 8

def highlight(current_selection, colums, rows, current_grid, secondary_color, squares, grid_color, current_widget, old_selection, old_grid, select_color, below_mouse):
    to_redraw = []
    current_widget.color(FL_WHITE)
    to_redraw.append(current_widget)
    if old_selection != None:
        for x in colums[old_selection[0]]:
            x.color(FL_WHITE)
            to_redraw.append(x)
        for y in rows[old_selection[1]]:
            y.color(FL_WHITE)
            to_redraw.append(y)
        if old_grid != None:
            for z in squares[old_grid]:
                z.color(FL_WHITE)
                to_redraw.append(z)
    if current_selection != None:
        for count, x in enumerate(colums[current_selection[0]]):
            if count != current_selection[1]:
                x.color(secondary_color)
                to_redraw.append(x)
        for count, y in enumerate(rows[current_selection[1]]):
            if count != current_selection[0]:
                y.color(secondary_color)
                to_redraw.append(y)
        if current_grid != None:
            for z in squares[current_grid]:
                z.color(grid_color)
                to_redraw.append(z)
    current_widget = below_mouse
    current_widget.color(select_color)
    to_redraw.append(current_widget)
    #print(len(to_redraw) - len(set(to_redraw)), "redrawing elements culled")
    for x in set(to_redraw):
        x.redraw()

#variables