"""
657. Reboot Return to Origin

There is a robot start at position (0,0)
at the origin on a 2d plan.

Given a sequence of its moves, judge if this robot ends up at 
(0,0) after it completes its moves.

The move sequence is representetd by a string, 
and the character moves[i] represents its ith
move.

Valid moves are R (right), L (left), U (up), and D (down).

If the robot returns to the origin  after it finishes all 
of its moves, return true.
Otherwsie, return false.

Note: tthe way that the robot is facing is irrelevant. 
"R" will always make the roboot move once

Also assume the magnitude of the robot movement is the same
for each move.

Input: "UD"
Output: true 
Explanation: The robot moves up once, and then down once. 
All moves have the same magnitude, so it ended up at
 the origin where it started. Therefore, we return true.

 Example 2:

Input: "LL"
Output: false
Explanation: The robot moves left twice. It ends up two "moves" to 
the left of the origin. We return false because it is not at 
the origin at the end of its moves.


Goldman Sachs | Amazon
"""

from typing import List

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0,0]
        col_index = 0
        row_index = 1
        for i in moves:
            if i == 'U':
                pos[col_index] +=1
            elif i == 'D':
                pos[col_index]-=1
            elif i == 'R':
                pos[row_index]+=1
            elif i == 'L':
                pos[row_index]-=1            
            print(pos)
        return pos[col_index] == 0 and pos[row_index] == 0


if __name__ == "__main__":
    input = "LL"
    expected = True
    s = Solution()
    a = s.judgeCircle(input)
    print(a,expected)