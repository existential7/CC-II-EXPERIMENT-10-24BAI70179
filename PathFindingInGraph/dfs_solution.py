"""
Find if Path Exists in Graph - DFS
Student: Aryan
UID: 24BAI70179
"""

def build_adj_list(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def dfs_has_path(n, edges, source, destination, visited=None):
    if visited is None:
        visited = [False] * n
    if source == destination:
        return True
    if visited[source]:
        return False
    visited[source] = True
    adj = build_adj_list(n, edges)
    for nei in adj[source]:
        if dfs_has_path(n, edges, nei, destination, visited):
            return True
    return False

# Test cases
test_cases = [
    (3, [[0,1],[1,2],[2,0]], 0, 2),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5),
    (1, [], 0, 0)
]

for i, (n, edges, src, dst) in enumerate(test_cases, 1):
    result = dfs_has_path(n, edges, src, dst)
    print(f"Test {i}: {result}")
