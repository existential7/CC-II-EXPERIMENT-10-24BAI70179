"""
Find if Path Exists in Graph - BFS
Student: Aryan
UID: 24BAI70179
"""

from collections import deque

def build_adj_list(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def bfs_has_path(n, edges, source, destination):
    if source == destination:
        return True
    adj = build_adj_list(n, edges)
    visited = [False] * n
    q = deque([source])
    visited[source] = True
    while q:
        node = q.popleft()
        for nei in adj[node]:
            if not visited[nei]:
                if nei == destination:
                    return True
                visited[nei] = True
                q.append(nei)
    return False

# Test cases
test_cases = [
    (3, [[0,1],[1,2],[2,0]], 0, 2),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5),
    (1, [], 0, 0)
]

for i, (n, edges, src, dst) in enumerate(test_cases, 1):
    result = bfs_has_path(n, edges, src, dst)
    print(f"Test {i}: {result}")
