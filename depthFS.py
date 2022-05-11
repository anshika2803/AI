import time
from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
        self.visited = [False]*V
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def DFS(self, s, d, path, paths):
        self.visited[s] = True
        path.append(s)
        
        if s == d:
            paths[tuple(path)] = len(path)
        
        for ver in self.adj[s]:
            if not self.visited[ver]:
                self.DFS(ver, d, path, paths)
        
        path.pop(-1)
        self.visited[s] = False
    
    def shortestPath(self, s, d):
        path = []
        allPaths = dict()
        self.DFS(s, d, path, allPaths)
        
        short = float('inf')
        shortest_path = []
        for p, l in  allPaths.items():
            if short > l:
                short = l
                shortest_path = p
        
        print("Shortest Path: ", shortest_path)

v = int(input("Enter the no. of Vertices: "))
e = int(input("Enter the no. of Edges: "))

g = Graph(v)

for i in range(e):
    inp = input("Enter the vertices of edge {}: ".format(i+1))
    edge = list(map(int, inp.split()))
    g.addEdge(edge[0], edge[1])

s = int(input("Enter the source: "))
d = int(input("Enter the destination: "))

begin = time.time()
g.shortestPath(s, d)

time.sleep(1)
end = time.time()
print("Time taken by DFS: ", end - begin)
