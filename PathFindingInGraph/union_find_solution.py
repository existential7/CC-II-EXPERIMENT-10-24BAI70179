"""
Find if Path Exists in Graph - Union-Find
Student: Aryan
UID: 24BAI70179
"""

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

def union_find_has_path(n, edges, source, destination):
    if source == destination:
        return True
    dsu = DisjointSet(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.find(source) == dsu.find(destination)

# Test cases
test_cases = [
    (3, [[0,1],[1,2],[2,0]], 0, 2),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5),
    (1, [], 0, 0)
]

for i, (n, edges, src, dst) in enumerate(test_cases, 1):
    result = union_find_has_path(n, edges, src, dst)
    print(f"Test {i}: {result}")
