
from node import Node
from tree import Tree
from random import randrange

if __name__ == "__main__":

   arr = [randrange(1,100) for i in range(100)]
   #[print(i) for i in arr]
   tree = Tree(verbose=False)
   [tree.addNode(i) for i in arr]
   print("tree height: ", tree.getHeight())
   tree.display()
   tree.getInOrder()
   tree.getPreOrder()
   tree.findValue(10)