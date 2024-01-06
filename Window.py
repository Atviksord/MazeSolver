from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self,width,height):
        self.root = Tk()
        self.root.title('MazeSolverBot')
        self.canvas = Canvas(self.root,width=width,height=height,background='black')
        self.canvas.pack(fill=BOTH,expand=1)
        self.running = False
        self.root.protocol('WM_DELETE_WINDOW',self.close)
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('Program exited')
    def close(self):
        self.running = False
    def draw_line(self,line,fill_color='Black'):
        line.draw(self.canvas,fill_color)