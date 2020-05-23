import threading,queue

#from queue import PriorityQueue, Queue, deque

# https://docs.python.org/3/library/queue.html

class Example:
    def __init__(self):
        self.q = queue.Queue()
    
    def enequeue(self,item):
        self.q.put(item)
    
    def deque(self):
        return self.q.get()
    
    def peek(self):
        if self.q.qsize() < 0:
            return None
        return self.q.queue[0]

    def print(self):
        for item in self.q.queue:
            print(item,end=", ")


if __name__ == "__main__":
    e = Example()

    e.enequeue(5)
    e.enequeue(10)
    e.enequeue(15)
    e.enequeue(20)
    print(e.peek())
    e.print()
