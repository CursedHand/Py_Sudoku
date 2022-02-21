def printgrid(grid):
    for x in grid:
        for y in x:
            print(y, " ", end="")
        print("")


def unassigned(grid):       #Returns the coords of the next empty cell, otherwise returns -1, -1
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col == ".":
                return y,x
    return -1, -1

def valid(grid, num, y_cord, x_cord):
    not_row = False
    not_col = False
    not_square = True

    if str(num) not in grid[y_cord]:
        not_row = True

    in_col = []
    for row in grid:
        if row[x_cord] != ".":
            in_col.append(row[x_cord])
    if str(num) not in in_col:
        not_col = True


    square_y = (y_cord//3)*3+1
    square_x = (x_cord//3)*3+1


    for y in [square_y-1, square_y, square_y+1]:
        for x in [square_x-1, square_x, square_x+1]:
            if grid[y][x] == str(num):
                not_square = False


    if not_row == True and not_col == True and not_square == True:
        return True
    return False

def backfill(grid):
    y, x = unassigned(grid)

    if y == -1 and x == -1: #If it is solved
        return grid

    for i in range(1, 10):
        if valid(grid, i, y, x):
            grid[y][x] = str(i)
            if backfill(grid):
                return grid
            grid[y][x] = "."

    return False


if __name__ == "__main__":

    grid=[
        [".","8",".","5","3",".","2","7","6"],
        [".","5",".","6",".",".",".",".","."],
        ["6","1","3",".",".",".",".",".","."],
        [".",".","6",".","5",".",".",".","."],
        [".","3","2",".",".",".","7",".","1"],
        ["7","4","5",".",".","8","6","9","3"],
        [".","7",".","9","6",".","5",".","."],
        ["4",".",".","1","8",".",".","6","7"],
        ["5",".",".",".",".","4","8","2","9"]
    ]




    printgrid(grid)
    print(backfill(grid))
    printgrid(grid)