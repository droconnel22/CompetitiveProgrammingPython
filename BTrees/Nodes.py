class Node:
    def __init__(self, data):
        self.Left = None
        self.Right = None
        self.Data = data
        self.IsTouched = False

    def insert(self, value):
        if value <= self.Data:
            if self.Left is None:
                self.Left = Node(value)
            else:
                self.Left.insert(value)
        else:
            if self.Right is None:
                self.Right = Node(value)
            else:
                self.Right.insert(value)

    def inOrder(self):
        if self.Left is not None:
            self.Left.inOrder()
        print(self.Data)
        if self.Right is not None:
            self.Right.inOrder()
    
    def preOrder(self):
        print(self.Data)
        if self.Left is not None:
            self.Left.preOrder()
        if self.Right is not None:
            self.Right.preOrder()
    
    def postOrder(self):
        if self.Left is not None:
            self.Left.postOrder()
        if self.Right is not None:
            self.Right.postOrder()
        print(self.Data)
    
    def find(self,value):
        if value == self.Data:
            return True
        elif value >= self.Data:
            if self.Right is not None:
                return self.Right.find(value)
            else:
                return False
        else:
            if self.Left is not None:
                return self.Left.find(value)
            else:
                return False
    
    def findNode(self,value):
        if value == self.Data:
            return self

        if value >= self.Data:
            if self.Right is not None:
                return self.Right.findNode(value)
        else:
            if self.Left is not None:
                return self.Left.findNode(value)
        return None

    def delete(self,value,previous):
        if self.Data == value:
            # found now delete
            #worst case
            if self.Right and self.Left:
                tempMin = self.Right.min_value_node()
                if previous.Left == tempMin:
                    previous.Left = tempMin.Right
                else:
                    previous.Right = tempMin.Right
                
                tempMin.Left = self.Left
                tempMin.Right = self.Right

                return tempMin

            else:
                if self.Left:
                    return self.Left
                else:
                    return self.Right
        
        elif self.Data < value:
            if self.Left:
                self.Left = self.Left.delete(value,self)
        else:
            if self.Right:
                self.Right = self.Right.delete(value,self)
        return self
   
    def min_value_node(self):
        if self.Left is None:
            return self
        else:
            return self.Left.min_value_node()

    def min_value(self):
        if self.Left is None:
            return self.Data            
        else:
            return self.Left.min_value()
    
    def max_Value(self):
        if self.Right is None:
            return self.Data
        else:
            return self.Right.max_Value()