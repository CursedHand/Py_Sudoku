from fltk import *
import time

class MyApp(Fl_Window):
    def __init__(self, x,y, w, h, label=None):
        Fl_Window.__init__(self, x, y, w, h, label)
        self.color(FL_BLACK)
        self.end()
        self.sep=10

    def handle(self, event):
        r=super().handle(event)
        if event==FL_SHORTCUT:
            if Fl.event_key()==FL_Up:
                if self.sep < self.w()-1: #max window size
                    self.sep +=1
                    self.redraw()
                return 1
            elif Fl.event_key()==FL_Down:
                if self.sep > 1: #min value 1
                    self.sep -=1
                    self.redraw()
                return 1
        return r

    def draw(self):
        Fl_Window.draw(self)

        fl_color(FL_RED)
        for x in range(0,self.w()+1,self.sep):
            fl_line(x,0,x,self.h())
        for y in range(0,self.h()+1, self.sep):
            fl_line(0,y,self.w(),y)

size=301
app = MyApp(0,0, size, size)
app.show()
Fl.run()