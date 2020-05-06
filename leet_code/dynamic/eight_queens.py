"""
Eight Queens

Write an algorithm to print all wasy of arranign eight queens
on an 8x8 chess baord so that none of them share the same row,
column, or diagnoal.

In this case diagonal meals all diagonals, not just the 
two that bisect the baord

We have eight queens which must be lined up on a
8x8 chessboard such taht none share the same row,
column or diagonal

So we know that each row and column (and diagonal)
must be used exactly once.




"""

def solve_eight_queens():
    row  = 0
    columns = [0 for _ in range(8)]
    results = []
    return solve_eight_queens_helper(row,columns,results)

def solve_eight_queens_helper(row,columns,results):
    if row == 8:
        results.append(columns[:])
    else:
        for col in range(8):
            if check_valid(columns,row,col):
                # Place Queen
                columns[row] = col
                solve_eight_queens_helper(row+1,columns,results)
    return results

def check_valid(columns, row, col):
    for row2 in range(0,row):
        col2 = columns[row2]
        # Check if row2, col2 invalidates the row1 col1 as queens spot
        if col == col2:
            return False
        # Check diagonals - if the distance between the columns equals
        # the distance between rows then it is in same digaonal
        col_distance = abs(col2-col) 
        row_distance = row - row2
        if (col_distance == row_distance):
            return False
    return True

    


if __name__ == "__main__":
    r = solve_eight_queens()
    print(len(r))
    print(r)