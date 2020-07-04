"""
101. Symmetric Tree

Easy

Given a binary tree, check
whether it is a mirror of itself
(i.e. symmetric around its center)

mirror around its center

For example 
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Amazon LinkedIn
Bloomberg Facebook
Oracle Google
Microsoft


Follow up: Solve it both recursively and iteratively.

Tree
Depth First Search
Breath First Serach

"""
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        searched = []
        queue = []
        queue.append(root)
        while len(queue) > 0:
            current_node = queue.pop()
            if current_node.val in searched:
                searched.remove(current_node.val)
            else:
                searched.add(current_node.val)
            
            if current_node.right and current_node.left:
                queue.append(current_node.right)
                queue.append(current_node.left)
            elif current_node.right or current_node.left:
                return False

    def isSymmetric_ans(self, root: TreeNode) -> bool:
         return self.isMirror(root,root)
    
    def isMirror(self,leftSubtree,rightSubtree):
        if leftSubtree is None and rightSubtree is None:
            return True
        if leftSubtree is None or rightSubtree is None:
            return False
        return (leftSubtree.val == rightSubtree.val) and self.isMirror(leftSubtree.right,rightSubtree.left) and self.isMirror(leftSubtree.left, rightSubtree.right)


if __name__ == "__main__":
    s = Solution()
