class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        seen = set()

        def dfs(i,j):
            if i not in range(rows) or j not in range(cols) or grid[i][j] == 0 or (i, j) in seen:
                return 0
            seen.add((i, j))
            return (1 + dfs(i + 1, j) + dfs(i- 1, j) + dfs(i, j + 1) + dfs(i, j - 1))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = max(area, dfs(i,j))
        return area
                    

        