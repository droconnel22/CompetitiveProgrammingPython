

from collections import deque,defaultdict
from queue import Queue

class StackExample:
    def __init__(self):
        self.stack = []
    
    def make(self,items):
        for item in items:
            self.stack.append(item)
    
    def print_out(self):
        while len(self.stack):
            print(self.stack.pop(),end=", ")

class QueueExample:
    def __init__(self):
        self.q = deque()
    
    def make(self,items):
        for item in items:
            self.q.append(item)
    
    def print_out(self):
        while len(self.q):
            print(self.q.popleft(),end=", ")

class SuperQueueExample:
    def __init__(self):
        self.q = Queue()
    
    def make(self,items):
        for item in items:
            self.q.put(item)
    def print_out(self):
        while self.q.qsize() > 0:
            print(self.q.get(),end=", ")



if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]
    se = StackExample()
    se.make(l)
    se.print_out()
    print("\n---")
    qe = QueueExample()
    qe.make(l)
    qe.print_out()
    print("\n---")
    se = SuperQueueExample()
    se.make(l)
    se.print_out()
