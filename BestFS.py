from collections import defaultdict
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
    
    def addEdge(self, u, v, h2):
        self.adj[u].append((v, h2))  
    
    def bestFirst(self, s, d, h1):
        success = False 
        open = [(s, h1)]
        closed = []
        
        while open and not success:
            t = open.pop(0)
            print(t[0], end = " ")
            if t[0] == d:
                success = True
                closed.append(t)
            else:
                closed.append(t)
                for neighbor in self.adj[t[0]]:
                    if neighbor not in open and neighbor not in closed:
                        open.append(neighbor)
                open.sort(key = lambda  t: t[1])            
    

v = int(input("Enter the no. vertices: "))
g = Graph(v)

heuristics = dict()
for i in range(v):
    ver_h = input("Enter vertex {} and its heuristic: ". format(i+1)).strip().split()
    heuristics[ver_h[0]] = int(ver_h[1])
    # print(ver_h[0], int(ver_h[1]))

e = int(input("Enter the no. edges: "))
for i in range(e):
    edge = input("Enter the vertices of edge {}: ". format(i+1)).strip().split()
    # print(heuristics[edge[0]], heuristics[edge[1]])
    g.addEdge(edge[0], edge[1], heuristics[edge[1]])

s = input("Enter the source: ")
d = input("Enter the destination: ")
g.bestFirst(s, d, heuristics[s])
