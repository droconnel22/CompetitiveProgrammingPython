"""
155. Min Stack

Design a stack that support push pop top and retriving the min
element in constant time

push(x) push an element onto a stack

pop() removes thte lement on the top of the stack

top() get the top element

getMin() - retreive the min element in the stack

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

Methods pop, top and getMin operations
 will always be called on non-empty stacks.

 Amazon Bloomberg Microsoft Apple Oracle
 Adobe Google Walmart Labs Netflix

 Stack | Design

Consider each node in the stack having a minimum value. (Credits to
"""

from collections import defaultdict, OrderedDict,deque
from queue import Queue


class MinStack:

    def __init__(self):
        self.stack = []
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        return self.stack.pop()
        
    #Get the top element.
    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if len(self.stack):
            return sorted(self.stack)[0]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())
    ms.pop()
    print(ms.top())
    print(ms.getMin())