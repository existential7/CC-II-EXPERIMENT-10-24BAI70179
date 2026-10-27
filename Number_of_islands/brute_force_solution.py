"""
LeetCode #200 - Number of Islands
Approach: Brute Force (separate visited matrix + DFS)

Student: Aryan
UID: 24BAI70179
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        self.display(grid)

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        count = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if visited[r][c] or grid[r][c] == '0':
                return
            visited[r][c] = True
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        return count

    def display(self, grid):
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
    ]))  # Expected: 1

    print(sol.numIslands([
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]))  # Expected: 3

    print(sol.numIslands([["1"]]))  # Expected: 1
    print(sol.numIslands([["0"]]))  # Expected: 0
    print(sol.numIslands([["1", "0"], ["0", "1"]]))  # Expected: 2
