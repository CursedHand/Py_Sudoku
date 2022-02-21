from fltk import *

import QoLfunctions
import DynamicHighlighting
import GenerateGrid
import Backtrackingtest

#BUG LIST
#   None

#FIXED --> drawn lines flicker


class Sudoku(Fl_Window):
    def __init__ (self,x,y,w,h, name):
        Fl_Window.__init__(self,x,y,w,h,name)
        self.width, self.height = w, h
        self.margin = 2 #Space betweeen center of lines and boxes
    
        self.select_color = fl_rgb_color(0,128,0)
        self.secondary_color = fl_rgb_color(0,255,127)
        self.grid_color = fl_rgb_color(50,205,50)

        self.create_menu()
        self.grid = GenerateGrid.create_grid(self.width, self.height, self.margin)
        self.rows, self.colums, self.squares = GenerateGrid.fill_grid(self.grid)

        self.current_widget = self.grid[0][0]
        self.current_selection = None
        self.old_selection = None
        self.current_grid = None
        self.old_grid = None

        self.assist = False

    def create_menu(self):
        self.menu = Fl_Menu_Bar(0,0,self.width,(self.height-self.width))
        self.menu.add("Window/Size/Small", 0, self.resize_cb, 0)
        self.menu.add("Window/Size/Medium", 0, self.resize_cb, 1)
        self.menu.add("Window/Size/Large", 0, self.resize_cb, 2)
        self.menu.add("Game/Highlight Assist", 0, self.highlightassist, None, FL_MENU_TOGGLE)
        self.menu.add("Game/Solve", 0, self.solve, None)

    def highlightassist(self, wid, empty):
        if self.assist == False:
            self.assist = True
        else:
            self.assist = False
            for x in self.grid:
                for y in x:
                    if y.color() != FL_WHITE:
                        y.color(FL_WHITE)
                        y.redraw()


    def solve(self, wid, empty):
        formatted_grid = self.formatgrid()
        solved = Backtrackingtest.backfill(formatted_grid)
        if solved == False:
            fl_message("Sudoku cannot be solved!")
        else:
            for y, row in enumerate(solved):
                for x, item in enumerate(row):
                    if self.rows[y][x].value() != "  " + item:
                        self.rows[y][x].textcolor(FL_RED)
                        self.rows[y][x].value("  " + item)

    def formatgrid(self):
        grid = []
        for y in self.rows:
            row = []
            for x in y:
                if x.value().replace(" ", "") != "":
                    row.append(x.value().replace(" ", ""))
                else:
                    row.append(".")
            grid.append(row)
        return grid

    def resize_cb(self, button, size):
        self.width, self.height = GenerateGrid.resize_cb(self, size, self.grid, self.menu, self.width, self.height, self.margin)

    def draw(self):
        Fl_Window.draw(self)
        fl_color(FL_BLACK)
        fl_line_style(FL_SOLID, 4)
        for x in range(2):  #Vertical Lines
            fl_line(int(self.width/3)*(x+1),(self.height-self.width),int(self.width/3)*(x+1),self.height)
        for x in range(2): #Horizontal Lines
            fl_line(0, int((self.width)/3)*(x+1)+(self.height-self.width), self.width, int((self.width)/3)*(x+1)+(self.height-self.width))



    def handle(self, event):
        for row_num, row in enumerate(self.grid):
            for col_num, box in enumerate(row):
                QoLfunctions.center_text(self, box)
                if box.color() == self.select_color:
                    if self.current_selection != [row_num, col_num]:
                        self.old_selection = self.current_selection
                        self.current_selection = [row_num, col_num]


        if self.assist == True:
            below_mouse = Fl_belowmouse()
            if self.current_selection != None:
                self.old_grid = self.current_grid
                self.current_grid = DynamicHighlighting.getcurrentgrid(self, self.current_selection)
            if below_mouse != None and below_mouse.y() >= (self.height-self.width):
                DynamicHighlighting.highlight(self.current_selection, self.colums, self.rows, self.current_grid, self.secondary_color, self.squares, self.grid_color, self.current_widget, self.old_selection, self.old_grid, self.select_color, below_mouse)
        
        return super().handle(event)




sudoku = Sudoku(0,0,711,761, "Sudoku")  #width should be divisable by 9 & height must be greater or = to width
sudoku.begin()
sudoku.show()
Fl.run()
