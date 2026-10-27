"""
LeetCode #200 - Number of Islands
Approach: Optimized - In-Place DFS (Flood Fill)

Student: Aryan
UID: 24BAI70179
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        display(grid)

        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count

    
def display(grid):
    print("Island Grid:")
    for row in grid:
        print(" ".join(row))
    print()

if __name__ == "__main__":
    sol = Solution()

    print(sol.numIslands([
        list("11110"),
        list("11010"),
        list("11000"),
        list("00000"),
    ])) 

    print(sol.numIslands([
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ])) 

    print(sol.numIslands([["1"]])) 
    print(sol.numIslands([["0"]])) 
    print(sol.numIslands([["1", "0"], ["0", "1"]]))
