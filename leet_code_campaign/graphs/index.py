from collections import defaultdict

class Graph:
    def __init__(self,is_directed=True):
        self.graph = defaultdict(list)
        self.is_directed = is_directed

    def insert_edge(self,v1,v2):
        self.graph[v1].append(v2)
        if not self.is_directed:
            self.graph[v2].append(v1)

    # O(V)
    def depth_first_search(self, v_current, v_target,searched=[]):
        if v_current in searched:
            return
        
        searched.append(v_current)
        if v_current == v_target:
            print('found!')
        else:
            for adj_node in self.graph[v_current]:
                self.depth_first_search(adj_node,v_target,searched)

    def depth_first_stack(self,start):    
        stack  = []
        searched = set()
        stack.append(start)
        
        while len(stack):
            current_node = stack[-1]
            stack.pop()

            if current_node in searched:
                continue
            
            print(current_node)
            searched.add(current_node)

            for adj_node in self.graph[current_node]:
                stack.append(adj_node)

    #O(V+E)
    def breath_first_search(self,start):
        queue = []
        searched = set()
        queue.append(start)

        while len(queue):
            current_node = queue.pop(0)
            #queue.remove(current_node)

            if current_node in searched:
                continue
            
            print(current_node,end=",")
            searched.add(current_node)

            for adj_node in self.graph[current_node]:
                queue.append(adj_node)



        

    def print_graph(self):
        for node in self.graph:
            for adj_node in self.graph[node]:
                print("%s -> %s" % (node, adj_node) if self.is_directed else "%s <-> %s" % (node, adj_node))

g = Graph()
g.insert_edge(2,1)
g.insert_edge(2,5)
g.insert_edge(5,6)
g.insert_edge(5,8)
g.insert_edge(6,9)
#g.print_graph()

g.depth_first_search(2,6)
g.depth_first_stack(2)
g.breath_first_search(2)

# g = Graph()
# g.insert_edge(1,2)
# g.insert_edge(2,3)
# g.insert_edge(4,5)
# g.print_graph()