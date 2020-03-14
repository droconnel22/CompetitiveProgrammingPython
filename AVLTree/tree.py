

from node import Node
from typing import List, Dict


class Tree:
    def __init__(self, verbose=False):
        self.root = None
        self.verbose = verbose
    
    def addNode(self,value):
        if value is None:
            return
        if self.root is None:
            self.root = Node(value)
        else:
            self._addNode(self.root,value)
    
    def _addNode(self, node, value):
        if value is None:
            return
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._addNode(node.left,value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._addNode(node.right,value)
        else:
            if self.verbose:
                print("exists")
    
    def getHeight(self):
        if self.root is None:
            return 0
        return self._getHeight(self.root,0)
    
    def _getHeight(self, node,height):
        if node is None:
            return height
        else:      
            left = self._getHeight(node.left,height+1)
            right = self._getHeight(node.right,height+1)        
            return max(left,right)

    def getInOrder(self):
        if self.root is None:
            if self.verbose:
                print("Empty")
            return 
        else:
            print("In Order: ")
            self._getInOrder(self.root)
            print()
    
    def _getInOrder(self,node):
        if node is not None:
            self._getInOrder(node.left)
            print(node.value," -> ", end = " ")
            self._getInOrder(node.right)

    def getPreOrder(self):
        if self.root is None:
            if self.verbose:
                print("Empty")
            return 
        else:
            print("Pre Order: ")
            self._getPreOrder(self.root)
            print()
    
    def _getPreOrder(self, node):
        if node is not None:
            print(node.value," -> ", end = " ")
            self._getInOrder(node.left)           
            self._getInOrder(node.right)

    
    def display(self):
        if self.root is None:
            print("empty tree")
        else:
            resultDict = {}
            height = 0
            self._display(self.root,height,resultDict)
            max = 0
            for key,val in resultDict.items():
                if(len(val) > max):
                    max = len(val)
            max *=2
            level = 2
            for key, val in resultDict.items():
                level *=2
                for item in val:
                    print(" "*(max//level),item, end="")
                print()

    def _display(self, node, height, resultDict):
        if node is None:
            return
        else:   
            if height not in resultDict:
                resultDict[height] = []
            resultDict[height].append(node.value)
            self._display(node.left,height+1,resultDict)
            self._display(node.right,height+1,resultDict)

    def findValue(self, value) -> str:
        if value is None:
            return "Value Does Not Exist"
        elif self.root is None:
            return "Tree is empty"
        else:
            return self._findValue(self.root, value)
    
    def _findValue(self, node, value):
        if node is None:
            if self.verbose:
                print("nope!")
            return None
        elif node.value == value:
            if self.verbose:
                print("Found node!")
            return node
        elif node.value > value:
            return self._findValue(node.left,value)
        elif node.value < value:
            return self._findValue(node.right,value)


    def deleteValue(self, value):
        if value is None:
            if self.verbose:
                print("value is null!")
            return
        else:
            if self.root is None:
                if self.verbose:
                    print("Tree is empty")
                return
            else:
                self._deleteValue(self.root,value)
    
    def _deleteValue(self, node, value):
        if node is None:
            if self.verbose:
                print("not here!")
            return
        if node.left.value == value:
             """
             val to delete is 3:
                2
              3  5
             1 4  
             """
            toDeleteNode = node.left
            if toDeleteNode.right is not None:
                node.left = toDeleteNode.right
                findDeleteLeftChildHome = toDeleteNode.right.left
                while findDeleteLeftChildHome is not None:
                    findDeleteLeftChildHome = findDeleteLeftChildHome.left
                findDeleteLeftChildHome.left = toDeleteNode.left 
            else:
                node.left = toDeleteNode.left
        else if node.right.value == value:
            toDeleteNode = node.right
            if toDeleteNode.left is not None:
                node.right = toDeleteNode.left
                findDeleteRightChildHoome toDeleteNode.left.right
                while findDeleteLeftChildHome is not None:
                    findDeleteLeftChildHome = findDeleteLeftChildHome.right
                findDeleteLeftChildHome.right = toDeleteNode.right
            else:
                node.right = toDeleteNode.right
        else if node.value < value:
            self._deleteValue(node.right,value)
        else if node.value > value:
            self._deleteValue(node.left,value)
        else:
            if self.verbose:
                print("oops")
        
        

        
        
        


            