
"""
Robot in a grid. 
Imagine a robot sitting on the upper left corner of grid with r rows
and c columns.
 The robot can only move in two directions, right and down, but certain
cells are off limits such a that he robot cannnot step on them.

 Design an alogrithm to
find a path for the robot from the top left to the bottom right.

Hints
if we picture this grid, the only way to move to spot (r,c)
is by moving to one of the adjacent spots
(r-1,c)
(r,c-1)
So we need to find a path either 
(r-1,c)
(r,c-1)

HOw do we find a path to those spots?
path is top left to bottom right

"""

def find_a_path(maze):
    """
    Maze is a boolean matrix
    """
    if (maze is None or len(maze) == 0):
        return None
    
    path = []
    failed_points = set()
    if (get_Path(maze,len(maze)-1,len(maze[0])-1,path,failed_points)):
        return path
    else:
        return None

def get_Path(maze, row,col, path,failed_points):
    if(col < 0 or row < 0 or maze[row][col] is False):
        return False
    
    atOrigin = (row == 0) and (col == 0)

    if((row,col) in failed_points):
        return False

    if(atOrigin or get_Path(maze,row,col-1,path,failed_points) or get_Path(maze,row-2,col,path,failed_points)):
        path.append((row,col))
        return False
    else:
        failed_points.add((row,col))
        return False


if __name__ == '__main__':
    print("Hello World")