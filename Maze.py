
from tkinter import Tk, BOTH, Canvas
from Point import Point
from Line import Line
from Cell import Cell
import time
import random
class Maze:
    def __init__(self,win,cellwidth,cellheight):
        self.cellwidth = cellwidth
        self.cellheight = cellheight
        self.grid = []
        self.win = win
        self.seed = 0
        if self.seed != None:
             self.seed = random.seed(0)
    
    
    def create_cells(self,cellcount):
            self.grid = [[Cell(canvas = self.win,p1 = Point(0,0),p2= Point(0,0)) for _ in range(cellcount)] for _ in range(cellcount)]
            
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                     self.grid[i][j]._x1 = 10 + (j * self.cellwidth)
                     self.grid[i][j]._y1 = 10 + (i * self.cellheight)
                     self.grid[i][j]._x2 = self.grid[i][j]._x1 + self.cellwidth
                     self.grid[i][j]._y2 = self.grid[i][j]._y1 + self.cellheight
                     
    def draw_cells(self):
         if self.win is None:
              return
         for i in range(len(self.grid)):
              for j in range(len(self.grid[i])):
                self.grid[i][j].draw()
                
    
    def animate(self):
         if self.win is None:
              return
         self.win.redraw()
         time.sleep(0.05)
    def BREAK_ENTRANCE_AND_EXIT(self, testing = False):
        
         self.grid[0][0].leftwall = False
         self.grid[-1][-1].rightwall = False
         
         if not testing:
            self.draw_cells()
            self.draw_cells()
            self.win.redraw()
    def BREAK_WALLS_R(self, i, j):
         self.grid[i][j].visited = True
         while True:
              visiting = []
              
              if i-1 >= 0:
                   if self.grid[i-1][j].visited != True:
                        visiting.append((i-1,j))
    
              if i+1 < len(self.grid):
                   if self.grid[i+1][j].visited != True:
                        visiting.append((i+1,j))
  
              if j-1 >= 0:
                   if self.grid[i][j-1].visited != True:
                        visiting.append((i,j-1))
               
              if j+1 < len(self.grid[i]):
                   if self.grid[i][j+1].visited != True:
                         visiting.append((i,j+1))
                #Add cells to visiting to visit.
              if not visiting:
                   break
              choice_i,choice_j = random.choice(visiting)
              if choice_j == j+1: #if the random choice is right neighbour
                   self.grid[i][j+1].leftwall = False
                   self.grid[i][j].rightwall = False
                   self.draw_cells()
                   self.animate()
                   self.BREAK_WALLS_R(choice_i,choice_j)
                   
              elif choice_j == j-1: #left neighbour
                   self.grid[i][j-1].rightwall = False
                   self.grid[i][j].leftwall = False
                   self.draw_cells()
                   self.animate()
                   self.BREAK_WALLS_R(choice_i,choice_j)
                   
              elif choice_i == i+1: #bottom neighbour
                   self.grid[i+1][j].topwall = False
                   self.grid[i][j].bottomwall = False
                   self.draw_cells()
                   self.animate()
                   self.BREAK_WALLS_R(choice_i,choice_j)
                   
              elif choice_i == i-1:
                   self.grid[i-1][j].bottomwall = False
                   self.grid[i][j].topwall = False
                   self.draw_cells()
                   self.animate()
                   self.BREAK_WALLS_R(choice_i,choice_j)
    def reset_cells_visited(self):
         for i in range(len(self.grid)):
              for j in range(len(self.grid[i])):
                   self.grid[i][j].visited = False

    def solve(self):     
              solved = self.solve_r(i = 0, j = 0)
              if solved:
                   return True
              else:
                   return False
    
    def solve_r(self,i,j):
         self.animate()
         self.grid[i][j].visited = True
         if self.grid[-1][-1].visited == True:
              return True
         for _ in range(4):
              if j+1 < len(self.grid[i]):
                    if not self.grid[i][j+1].leftwall and not self.grid[i][j+1].visited: #left
                         self.grid[i][j].draw_move(self.grid[i][j+1])
                         if self.solve_r(i,j+1):
                         
                              return True
                         else:
                              self.grid[i][j].draw_move(self.grid[i][j+1],undo = True)
              
              if j-1 >= 0:
                    if not self.grid[i][j-1].rightwall and not self.grid[i][j-1].visited: # right
                         self.grid[i][j].draw_move(self.grid[i][j-1])
                         if self.solve_r(i,j-1):
                         
                              return True
                         else:
                              self.grid[i][j].draw_move(self.grid[i][j-1],undo = True)

              if i+1 < len(self.grid):
                    if not self.grid[i+1][j].topwall and not self.grid[i+1][j].visited: #bottom
                         self.grid[i][j].draw_move(self.grid[i+1][j])
                         if self.solve_r(i+1,j):
                         
                              return True
                         else:
                              self.grid[i][j].draw_move(self.grid[i+1][j],undo = True)

              if i-1 >= 0:
                    if not self.grid[i-1][j].bottomwall and not self.grid[i-1][j].visited: #top
                         self.grid[i][j].draw_move(self.grid[i-1][j])
                         if self.solve_r(i-1,j):
                              return True
                         else:
                              self.grid[i][j].draw_move(self.grid[i-1][j],undo = True)
 

                
   

              
              

              



         
         
         
                 

        


   