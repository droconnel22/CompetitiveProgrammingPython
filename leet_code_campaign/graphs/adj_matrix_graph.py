from collections import defaultdict

class Graph:
    def __init__(self,num_of_nodes):
        self.num_of_nodes = num_of_nodes+1
        self.graph = [
            [   0 for x in range(num_of_nodes+1)]
                for y in range(num_of_nodes+1)
            ]

    def insert_edge(self,v1,v2):
        if self._check_range(v1) or self._check_range(v2):
            return
        self.graph[v1][v2] = 1

    def _check_range(self,v):
        return v < 0 or v > self.num_of_nodes

    def print_graph(self):
        for i in range(self.num_of_nodes):
            for j in range(self.num_of_nodes):
                if self.graph[i][j] == 1:
                    print(i,'->',j)

g = Graph(5)

g.insert_edge(1,2)
g.insert_edge(2,3)
g.insert_edge(4,5)

g.print_graph()