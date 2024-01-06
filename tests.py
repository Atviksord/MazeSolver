import unittest
from Maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        cell_width = 10
        cell_height = 10
        m1 = Maze(None,cell_width, cell_height,)
        m1.create_cells(num_cols)  # note that `create_cells` will create a square grid with `num_cols` rows and columns
        # validate that all the rows and columns have been created
        self.assertEqual(
            len(m1.grid),
            num_cols,
        )
        for row in m1.grid:
            self.assertEqual(
                len(row),
                num_rows,
            )
    def test_break_entrance_and_exit(self):
        num_cols = 10
        num_rows = 10
        cell_width = 10
        cell_height = 10
        m2 = Maze(None, cell_width, cell_height)
        m2.create_cells(num_cols)

        m2.BREAK_ENTRANCE_AND_EXIT(testing=True)
        
        # Verify that the left wall of the first cell is removed (entrance).
        self.assertFalse(m2.grid[0][0].leftwall)

        # Verify that the right wall of the last cell is removed (exit).
        self.assertFalse(m2.grid[num_cols-1][num_rows-1].rightwall)
    def test_reset_cells_visited(self):
        m2 = Maze(None,50,50)
        m2.create_cells(20)
        m2.grid[0][8].visited = True
        m2.grid[2][10].visited = True
        m2.grid[3][10].visited = True
        m2.grid[7][10].visited = True
        m2.grid[0][6].visited = True
        m2.reset_cells_visited()
        for row in m2.grid:
            for cell in row:
                assert cell.visited == False, 'Not all cells were reset'

    
if __name__ == "__main__":
    unittest.main()