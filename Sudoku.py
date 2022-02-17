from fltk import *
import QoLfunctions

#BUG LIST
#FIXED --> drawn lines flicker (force lines to be on top?)


class Sudoku(Fl_Window):
    def __init__ (self,x,y,w,h, name):
        Fl_Window.__init__(self,x,y,w,h,name)
        self.width, self.height = w, h
        self.select_color = fl_rgb_color(121, 235, 121)
        self.secondary_color = fl_rgb_color(188, 245, 188)

        self.create_menu()
        self.create_grid()
        self.fill_grid()

        self.current_widget = self.grid[0][0]
        self.current_selection = None
        self.old_selection = None

    def create_menu(self):
        self.menu = Fl_Menu_Bar(0,0,self.width,(self.height-self.width))
        self.menu.add("Window/Size/Small", 0, self.resize_cb, 0)
        self.menu.add("Window/Size/Medium", 0, self.resize_cb, 1)
        self.menu.add("Window/Size/Large", 0, self.resize_cb, 2)
        self.menu.add("Game")

    def create_grid(self):
        self.grid = []
        box_size = int(self.width/9)
        for col in range(9):
            row_list = []
            for row in range(9):
                if col == 2 or col == 5:
                    if row != 2 and row != 5 and row != 3 and row != 6:
                        row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width), box_size-2, box_size))
                    elif row == 2 or row == 5:
                        row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width), box_size-2, box_size-2))
                    else:
                        row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width)+2, box_size-2, box_size-2))
                elif col == 3 or col == 6:
                    if row != 3 and row != 6 and row != 2 and row != 5:
                        row_list.append(Fl_Input((box_size*col)+2, (box_size*row)+(self.height-self.width), box_size-2, box_size))
                    elif row == 3 or row == 6:
                        row_list.append(Fl_Input((box_size*col)+2, ((box_size*row)+(self.height-self.width))+2, box_size-2, box_size-2))
                    else:
                        row_list.append(Fl_Input((box_size*col)+2, ((box_size*row)+(self.height-self.width)), box_size-2, box_size-2))
                elif row == 2 or row == 5:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width), box_size, box_size-2))
                elif row == 3 or row == 6:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width)+2, box_size, box_size-2))
                else:
                    row_list.append(Fl_Input((box_size*col), (box_size*row)+(self.height-self.width), box_size, box_size))
                row_list[-1].maximum_size(3)
                row_list[-1].textsize(43)
                row_list[-1].box(FL_THIN_UP_BOX)
            self.grid.append(row_list)



    def fill_grid(self):

        self.squares = [[], [], [], [], [], [], [], [], []]
        self.rows = [[], [], [], [], [], [], [], [], []]
        self.colums = [[], [], [], [], [], [], [], [], []]

        for col_num, row in enumerate(self.grid):       #adds button to respective sqare, row, and collum list. Left to right, top to bottom
            for row_num, box in enumerate(row):
                if col_num <= 2:
                    if row_num <= 2:
                        self.squares[0].append(box)
                    if row_num > 2 and row_num <= 5:
                        self.squares[3].append(box)
                    if row_num > 5 and row_num <= 8:
                        self.squares[6].append(box)
                elif col_num > 2 and col_num <= 5:
                    if row_num <= 2:
                        self.squares[1].append(box)
                    if row_num > 2 and row_num <= 5:
                        self.squares[4].append(box)
                    if row_num > 5 and row_num <= 8:
                        self.squares[7].append(box)
                elif col_num > 5 and col_num <= 8:
                    if row_num <= 2:
                        self.squares[2].append(box)
                    if row_num > 2 and row_num <= 5:
                        self.squares[5].append(box)
                    if row_num > 5 and row_num <= 8:
                        self.squares[8].append(box)

                self.rows[row_num].append(box)
                self.colums[col_num].append(box)



    def resize_cb(self, button, size):
        if size == 0: #Small
            self.size(450, 500)
            self.width, self.height = 450, 500
            for row in self.grid:
                for box in row:
                    box.textsize(25)
        elif size == 1: #Medium
            self.size(711, 761)
            self.width, self.height = 711, 761
            for row in self.grid:
                for box in row:
                    box.textsize(43)
        else:   #Large
            self.size(918, 968)
            self.width, self.height = 918, 968
            for row in self.grid:
                for box in row:
                    box.textsize(55)
        self.current_size = size 


        boxsize = int(self.width/9)
        c = 0
        for row in self.grid:
            r = 0
            for but in row:
                if c == 2 or c == 5:
                    but.resize(boxsize*c, boxsize*r+(self.height-self.width), boxsize-2, boxsize)
                elif c == 3 or c == 6:
                    but.resize((boxsize*c)+2, boxsize*r+(self.height-self.width), boxsize-2, boxsize)
                else:
                    but.resize(boxsize*c, boxsize*r+(self.height-self.width), boxsize, boxsize)
                r += 1
            c += 1

        self.menu.size(self.width, self.height-self.width)
        self.redraw()


    def draw(self):
        Fl_Window.draw(self)
        fl_color(FL_BLACK)
        fl_line_style(FL_SOLID, 4)
        for x in range(2):  #Vertical Lines
            fl_line(int(self.width/3)*(x+1),(self.height-self.width),int(self.width/3)*(x+1),self.height)
        for x in range(2): #Horizontal Lines
            fl_line(0, int((self.width)/3)*(x+1)+(self.height-self.width), self.width, int((self.width)/3)*(x+1)+(self.height-self.width))

    def handle(self, event):
        for row_num, row in enumerate(self.grid):       #adds button to respective sqare, row, and collum list. Left to right, top to bottom
            for col_num, box in enumerate(row):
                QoLfunctions.center_text(self, box)
                if box.color() == self.select_color:
                    if self.current_selection != [row_num, col_num]:
                        self.old_selection = self.current_selection
                        self.current_selection = [row_num, col_num]


        
        below_mouse = Fl_belowmouse()

        if below_mouse != None and below_mouse.y() >= (self.height-self.width):
            self.current_widget.color(FL_WHITE)
            self.current_widget.redraw()

            if self.old_selection != None:
                for x in self.colums[self.old_selection[0]]:
                    x.color(FL_WHITE)
                    x.redraw()
                for y in self.rows[self.old_selection[1]]:
                    y.color(FL_WHITE)
                    y.redraw()

            

            print(type(self.colums))
            if self.current_selection != None:
                for count, x in enumerate(self.colums[self.current_selection[0]]):
                    if count != self.current_selection[1]:
                        x.color(self.secondary_color)
                        x.redraw()

                for count, y in enumerate(self.rows[self.current_selection[1]]):
                    if count != self.current_selection[0]:
                        y.color(self.secondary_color)
                        y.redraw()



            self.current_widget = below_mouse
            self.current_widget.color(self.select_color)
            self.current_widget.redraw()
            print(self.current_selection)

        return super().handle(event)


sudoku = Sudoku(0,0,711,761, "Sudoku")  #width should be divisable by 9 & height must be greater or = to width


sudoku.begin()
sudoku.show()
Fl.run()
