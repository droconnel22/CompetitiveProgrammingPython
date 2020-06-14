"""

102. Binary Tree Level Order Traversal

BFS

Given a binary tree return the level order traversal of its 
nodes value ie from left too right level by level

For example
Given binary tree [3,9,20,null,null,15,7]

Amazon Microsoft Apple
LinkedIn Bloomberg Facebook

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        searched = set()
        result = {}
        
        def helper(current_node,searched,height,result):
            if current_node is None:
                return
            if current_node in searched:
                return
            #print(current_node.val)
            searched.add(current_node)
            if height not in result:
                result[height] = []
            result[height].append(current_node.val)
            helper(current_node.left,searched, height+1,result)
            helper(current_node.right, searched, height+1,result)
        
        helper(root,searched,0,result)
        return list(result.values())

if __name__ == "__main__":
    s = Solution()
    s.levelOrderthere()