"""
66 Binary Tree Zigzag Level Order Traversal

Medium

Given a binary tree

return the zigzag level order traversal
of its nodes' values
ie
from left to right
then right to left for the next level
and alternate inbetween

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

    1
   / \
  2   3
    /  \
   5   4

return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]


Amazon Microsft Facebook 
Qualtrics ByteDance
Apple Bloomberg LinkedIn
Samsung

"""

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_node(self, val):
        if self.left is None:
            self.left = TreeNode(val)
        elif self.right is None:
            self.right = TreeNode(val)
        else:
            if val < self.val:
                self.left.add_node(val)
            else:
                self.right.add_node(val)


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        memo = {}
        def helper(current_node,level,memo):
            if current_node is None:
                return memo
            if level in memo:
                memo[level].append(current_node.val)
            else:
                memo[level] = [current_node.val]
            
            if level % 2 == 0:
                helper(current_node.left,level+1,memo)
                helper(current_node.right,level+1,memo)
            else:
                helper(current_node.right,level+1,memo)
                helper(current_node.left,level+1,memo)

        helper(root,1,memo)
        return list(memo.values())
    
    def zigzagLevelOrderbfs(self,root: TreeNode) -> List[List[int]]:
        memo = {}
        searched = []
        queue = deque()
        level = 1
        queue.append(root)
        while len(queue) > 0:
            current_node = queue.pop()
            if current_node in searched:
                continue
            searched.append(current_node)
            if level in memo:
                memo[level].append(current_node.val)
            else:
                memo[level] = [current_node.val]
            if level % 2 == 0:
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            else:
                if current_node.right:
                    queue.append(current_node.right)
                if current_node.left:
                    queue.append(current_node.left)
            level+=1
        return list(memo.values())

        
    def zigzagLevelOrderans(self, root: TreeNode) -> List[List[int]]:
         q = deque()
         zag = False
         result = []
         while len(q) > 0:
             level = []
             for i in range(len(q)):
                if zag:
                    node = q.pop()
                    level.append(node.val)
                    if node.right:
                        q.appendleft(node.right)
                    if node.left:
                        q.appendleft(node.left)
                else:
                    node = q.popleft()
                    level.append(node.val)                   
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            result.append(level)
            zag = not zag
                
    

if __name__ == "__main__":
    s = Solution()
    arr = [3,9,20,15,7]
    root = TreeNode(arr[0])
    for i in range(1,len(arr)):
        root.add_node(arr[i])
    r = s.zigzagLevelOrderbfs(root)
    print(r)


    
    