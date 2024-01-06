from tkinter import Tk, BOTH, Canvas
from Window import Window
from Cell import Cell
from Point import Point
from Maze import Maze
def main():
    
    win = Window(800,600)
    
    
    maze = Maze(win,50,50)
    maze.create_cells(20)
    maze.draw_cells()
    maze.BREAK_ENTRANCE_AND_EXIT()
    maze.BREAK_WALLS_R(0,0)
    maze.reset_cells_visited()
    maze.solve()


    

    win.wait_for_close()


if __name__ == "__main__":
    main()

    