from operator import ge
from fltk import *

def create_grid(width, height, margin):

    grid = []
    for col in range(9):
        row_list = []
        for row in range(9):

            x, y, w, h = get_size(row, col, width, height, margin)
            row_list.append(Fl_Input(x, y, w, h))
            
            row_list[-1].maximum_size(3)
            row_list[-1].textsize(43)
            row_list[-1].box(FL_THIN_UP_BOX)
        grid.append(row_list)
    return grid

def get_size(row, col, width, height, margin):
    box_size = int(width/9)
    x_pos = box_size*col
    y_pos = box_size*row + height - width
    if row == 2 or row == 5:
        if col == 2 or col == 5:
            return(x_pos, y_pos, box_size-margin, box_size-margin)
        elif col == 3 or col == 6:
            return(x_pos+margin, y_pos, box_size-margin, box_size-margin)
        else:
            return(x_pos, y_pos, box_size, box_size-margin)
    elif row == 3 or row == 6:
        if col == 2 or col == 5:
            return(x_pos, y_pos+margin, box_size-margin, box_size-margin)
        elif col == 3 or col == 6:
            return(x_pos+margin, y_pos+margin, box_size-margin, box_size-margin)
        else:
            return(x_pos, y_pos+margin, box_size, box_size-margin)
    elif col == 2 or col == 5:
        return(x_pos, y_pos, box_size-margin, box_size)
    elif col == 3 or col == 6:
        return(x_pos+margin, y_pos, box_size-margin, box_size)
    else:
        return(x_pos, y_pos, box_size, box_size)


def resize_cb(Sudoku, size, grid, menu, width, height, margin):
    if size == 0: #Small
        Sudoku.size(450, 500)
        width, height = 450, 500
        for row in grid:
            for box in row:
                box.textsize(25)
    elif size == 1: #Medium
        Sudoku.size(711, 761)
        width, height = 711, 761
        for row in grid:
            for box in row:
                box.textsize(43)
    else:   #Large
        Sudoku.size(918, 968)
        width, height = 918, 968
        for row in grid:
            for box in row:
                box.textsize(55)
    menu.size(width, height-width)
    Sudoku.redraw()

    c = 0
    for row in grid:
        r = 0
        for but in row:
            x, y, w, h = get_size(r, c, width, height, margin)
            but.resize(x,y,w,h)
            r += 1
        c += 1
    Sudoku.redraw()
    return width, height




def fill_grid(grid):
    squares = [[], [], [], [], [], [], [], [], []]
    rows = [[], [], [], [], [], [], [], [], []]
    colums = [[], [], [], [], [], [], [], [], []]

    for col_num, row in enumerate(grid):       #adds button to respective sqare, row, and collum list. Left to right, top to bottom
        for row_num, box in enumerate(row):
            if col_num <= 2:
                if row_num <= 2:
                    squares[0].append(box)
                if row_num > 2 and row_num <= 5:
                    squares[3].append(box)
                if row_num > 5 and row_num <= 8:
                    squares[6].append(box)
            elif col_num > 2 and col_num <= 5:
                if row_num <= 2:
                    squares[1].append(box)
                if row_num > 2 and row_num <= 5:
                    squares[4].append(box)
                if row_num > 5 and row_num <= 8:
                    squares[7].append(box)
            elif col_num > 5 and col_num <= 8:
                if row_num <= 2:
                    squares[2].append(box)
                if row_num > 2 and row_num <= 5:
                    squares[5].append(box)
                if row_num > 5 and row_num <= 8:
                    squares[8].append(box)

            rows[row_num].append(box)
            colums[col_num].append(box)

    return rows, colums, squares