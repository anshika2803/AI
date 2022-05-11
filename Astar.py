from collections import defaultdict

heuristic = dict()
Graph = defaultdict(list)

def aStar(start, des):
    openSet = [start]
    closedSet = []
    g = {}
    parent = {}
    g[start] = 0
    parent[start] = None
    
    while openSet:
        n = None
        for v in openSet:
            if n == None or g[v] + heuristic[v] < g[n] + heuristic[n]:
                n = v
                print(n)
            if n == d or not Graph[n]:
                pass
            else:
                for m, w in Graph[n]:
                    if m not in openSet and m not in closedSet:
                        openSet.append(m)
                        parent[m] = n
                        g[m] = g[n] + w
                       
                    else:
                        if g[m] > g[n] + w:
                            g[m] = g[n] + w
                            parent[m] = n
                            
                            if m in closedSet:
                                closedSet.remove(m)
                                openSet.append(m)
        
        if n == None:
            print("Path doesn't exist!!!")
            return 
        
        if n == des:
            
            path = []
            
            while parent[n] != None:
                path.append(n)
                n = parent[n]
            
            path.append(s)
            print("Path found: {}".format(path[::-1]))
            # print(parent)
            return     
        openSet.remove(n)
        closedSet.append(n)       
                            

v = int(input("Enter the no. vertices: "))
for i in range(v):
    ver_h = input("Enter vertex {} and its heuristic: ". format(i+1)).strip().split()
    heuristic[ver_h[0]] = int(ver_h[1])

e = int(input("Enter the no. edges: "))
for i in range(e):
    edge = input("Enter the vertices of edge {} along with the weight: ". format(i+1)).strip().split()
    Graph[edge[0]].append((edge[1], int(edge[2])))
    
# print(Graph)

s = input("Enter the source: ")
d = input("Enter the destination: ")
aStar(s, d)
