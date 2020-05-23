


class PlateStack:
    def __init__(self):
        self.stack = []

    def push(self,x):
        self.stack.append(x)
    
    def pop(self):
        if(len(self.stack) > 0):
            # pop the first item
            self.stack.pop()
    
    def top(self):
        if(len(self.stack) == 0):
            return None
        return self.stack[-1]

    def getLen(self):
        return len(self.stack)


if __name__ == "__main__":
    plate_stack = PlateStack()
