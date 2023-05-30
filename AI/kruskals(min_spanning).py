class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n)) #store the parent of each element
        self.rank = [0] * n #store the child node or depth of element

    def find(self, x):
        if self.parent[x] != x: #if true ,x is not parent itself
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y) #(px and py) of the sets to which x and y belong, respectively.
        if px == py: # already in same set
            return False
        if self.rank[px] < self.rank[py]: #px has lower rank or depth
            self.parent[px] = py #px merged with py
        elif self.rank[px] > self.rank[py]: #py has lower rank or depth
            self.parent[py] = px  #py merged with px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal(graph):
    n = len(graph)
    edges = [(graph[i][j], i, j) for i in range(n) for j in range(i+1, n)] #tuple creation
    edges.sort()
    mst = set()
    dsu = DisjointSet(n)
    for w, u, v in edges: #weight w, the source node u, and the destination node v
        if dsu.union(u, v):
            mst.add((u, v, w))
    return mst
# Example graph represented as a 2D list
graph = [    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

# Compute minimum spanning tree using Kruskal's algorithm
mst = kruskal(graph)

# Output minimum spanning tree
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge[0], "-", edge[1], ":", edge[2])