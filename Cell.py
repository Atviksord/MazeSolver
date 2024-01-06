from Line import Line
from Point import Point
from tkinter import Tk, BOTH, Canvas
class Cell:
    def __init__(self,canvas,p1,p2,leftwall = True,rightwall = True,topwall = True,bottomwall = True,fill_color = '#00FF00'):
        self.leftwall = leftwall
        self.rightwall = rightwall
        self.topwall = topwall
        self.bottomwall = bottomwall
        self._x1 = p1.x
        self._x2 = p2.x
        self._y1 = p1.y
        self._y2 = p2.y
        self.win = canvas
        self.fill_color = fill_color
        self.undo = False
        self.visited = False
    def draw(self):
        if self.leftwall:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self.win.draw_line(line, 'black')

        if self.rightwall:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self.win.draw_line(line, 'black')

        if self.topwall:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self.win.draw_line(line, 'black')

        if self.bottomwall:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.win.draw_line(line, self.fill_color)
        else:
            line = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self.win.draw_line(line,'black')

    def draw_move(self,to_cell,undo=False): #draw a line between two cells, if the flag is False then it will be red, on traceback (same way, it will be put to grey)
        halflength = abs(self._x2 - self._x1)//2
        x_center = (halflength + self._x1)
        y_center = (halflength + self._y1)

        halflength2 = abs(to_cell._x2 - to_cell._x1)//2
        x_center2 = (halflength2 + to_cell._x1)
        y_center2 = (halflength2 + to_cell._y1)

        line_color = 'magenta' if not undo else 'yellow'

        line = Line(Point(x_center,y_center),Point(x_center2,y_center2))
        self.win.draw_line(line,line_color)
