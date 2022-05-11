import time
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
        self.visited = [False]*V
    
    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    
    def BFS(self, s, d):
        prev = dict()
        queue = [s]
        self.visited[s] = True
        
        while queue:
            t = queue.pop(0)
            # print(t, end = " ")
            
            for ver in self.adj[t]:
                if not self.visited[ver]:
                    prev[ver] = t
                    queue.append(ver)
                    self.visited[ver] = True
                    if ver == d:
                        break
        return prev
    
    def shortestPath(self, s, d):
        path = []
        prev = self.BFS(s, d)
        at = d
        
        while at != s:
            path.append(at)
            at = prev[at]
        
        path.append(s)
        print("Shortest path: ", path[::-1])
        
    
v = int(input("Enter the no. of Vertices: "))
e = int(input("Enter the no. of Edges: "))

g = Graph(v)

for i in range(e):
    inp = input("Enter the vertices edge {}: ".format(i+1))
    edge = list(map(int, inp.split()))
    g.addEdge(edge[0], edge[1])

s = int(input("Enter the source: "))
d = int(input("Enter the destination: "))

begin = time.time()
g.shortestPath(s, d)

time.sleep(1)
end = time.time()
print("Time taken by BFS: ", end - begin)
