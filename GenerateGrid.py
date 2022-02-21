from fltk import *

def create_grid(width, height):
    grid = []
    box_size = int(width/9)
    for col in range(9):
        row_list = []
        for row in range(9):
            if col == 2 or col == 5:
                if row != 2 and row != 5 and row != 3 and row != 6:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width), box_size-2, box_size))
                elif row == 2 or row == 5:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width), box_size-2, box_size-2))
                else:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width)+2, box_size-2, box_size-2))
            elif col == 3 or col == 6:
                if row != 3 and row != 6 and row != 2 and row != 5:
                    row_list.append(Fl_Input((box_size*col)+2, (box_size*row)+(height-width), box_size-2, box_size))
                elif row == 3 or row == 6:
                    row_list.append(Fl_Input((box_size*col)+2, ((box_size*row)+(height-width))+2, box_size-2, box_size-2))
                else:
                    row_list.append(Fl_Input((box_size*col)+2, ((box_size*row)+(height-width)), box_size-2, box_size-2))
            elif row == 2 or row == 5:
                row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width), box_size, box_size-2))
            elif row == 3 or row == 6:
                row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width)+2, box_size, box_size-2))
            else:
                row_list.append(Fl_Input((box_size*col), (box_size*row)+(height-width), box_size, box_size))
            row_list[-1].maximum_size(3)
            row_list[-1].textsize(43)
            row_list[-1].box(FL_THIN_UP_BOX)
        grid.append(row_list)
    return grid


def fill_grid(grid):

    grid[0][0].value("8")
    grid[3][0].value("1")
    grid[5][0].value("7")
    grid[6][0].value("4")
    grid[7][0].value("6")
    grid[8][0].value("9")

    grid[2][1].value("5")
    grid[3][1].value("3")
    grid[5][1].value("6")
    grid[7][1].value("8")

    grid[5][2].value("4")
    grid[7][2].value("3")
    grid[8][2].value("5")

    grid[0][3].value("9")
    grid[1][3].value("8")
    grid[4][3].value("7")
    grid[7][3].value("1")

    grid[0][4].value("2")
    grid[1][4].value("5")
    grid[2][4].value("7")
    grid[3][4].value("8")
    grid[4][4].value("3")
    grid[7][4].value("9")

    grid[1][5].value("1")
    grid[2][5].value("3")
    grid[6][5].value("8")
    grid[7][5].value("7")
    grid[8][5].value("2")

    grid[2][6].value("8")
    grid[6][6].value("9")

    grid[0][7].value("4")
    grid[1][7].value("2")
    grid[3][7].value("7")
    grid[5][7].value("3")
    grid[6][7].value("1")

    grid[1][8].value("6")
    grid[2][8].value("1")
    grid[3][8].value("9")
    grid[6][8].value("3")



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