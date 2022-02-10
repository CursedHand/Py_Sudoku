from fltk import *


class Sudoku(Fl_Window):
    def __init__ (self,x,y,w,h, name):
        Fl_Window.__init__(self,x,y,w,h,name)
        self.width = w
        self.height = h
        self.boxes = []
        box_size = int(w/9)
        for width in range(9):
            row = []
            for height in range(9):
                row.append(Fl_Button((box_size*width), (box_size*height)+(h-w), box_size, box_size))
            self.boxes.append(row)

        self.menu = Fl_Menu_Bar(0,0,w,(h-w))
        self.menu.add("Window/Size/Small", 0, self.resize_cb, 0)
        self.menu.add("Window/Size/Medium", 0, self.resize_cb, 1)

        self.menu.add("Window/Size/Large", 0, self.resize_cb, 2)

        self.menu.add("Game")



    def resize_cb(self, button, size):
        if size == 0: #Small
            self.size(450, 500)
            self.width, self.height = 450, 500

        elif size == 1: #Medium
            self.size(711, 761)
            self.width, self.height = 711, 761
        else:   #Large
            self.size(918, 968)
            self.width, self.height = 918, 968
        
        boxsize = int(self.width/9)
        r = 0
        for row in self.boxes:
            c = 0
            for but in row:
                but.resize(boxsize*r, boxsize*c+(self.height-self.width), boxsize, boxsize)
                c += 1
            r += 1

        self.menu.size(self.width, self.height-self.width)
        self.redraw()


    def draw(self):
        h = 500
        Fl_Window.draw(self)
        fl_color(FL_BLACK)
        fl_line_style(FL_SOLID, 4)
        for x in range(2):  #Vertical Lines
            fl_line(int(self.width/3)*(x+1),(self.height-self.width),int(self.width/3)*(x+1),self.height)
        for x in range(2): #Horizontal Lines
            fl_line(0, int((self.width)/3)*(x+1)+(self.height-self.width), self.width, int((self.width)/3)*(x+1)+(self.height-self.width))

    '''def handle(self, event):
        if event != 11:
            print(event)
        return super().handle(event)'''


sudoku = Sudoku(0,0,711,761, "Sudoku")  #width should be divisable by 9 & height must be greater or = to width


sudoku.begin()
sudoku.end()


sudoku.show()
Fl.run()