from enum import Enum

"""
Paint Fill
Implement the paint fill function taht one might see on many
image editing programs.
That is given a screen (represetned by a 2-d arry of colors)
a point, and a new color
fill in the surrounding area until the color changes from
the original color

"""
class Color(Enum):
    Black =1
    White = 2
    Red = 3
    Yellow = 4
    Green = 5
    Blue = 6


def paint_fill(screen, row,col, newColor):
    if(screen[row][col] is newColor):
        return False
    return paint_fill(screen,row,col[row][col],newColor)

def paint_fill(screen,row,col,currentColor,newColor):
    if(row < 0  or col < 0 or row >= len(screen) or col >= len(screen[row])):
        return False
    
    if(screen[row][col] == currentColor):
        screen[row][col] = newColor
        # Up
        paint_fill(screen,row-1,col,currentColor,newColor)
        # Right
        paint_fill(screen,row,col+1,currentColor,newColor)
        # Down
        paint_fill(screen,row+1,col,currentColor,newColor)
        #Left
        paint_fill(screen,row,col-1,currentColor,newColor)
    return True
    


if __name__ == "__main__":
    screen = [
        [Color.Red,Color.Blue,Color.Blue],
        [Color.Blue,Color.Blue,Color.Black],
        [Color.Blue,Color.Blue,Color.Blue]
    ]

    print(screen)
    if(paint_fill(screen,1,1,Color.Blue, Color.Green)):
        print(screen)
