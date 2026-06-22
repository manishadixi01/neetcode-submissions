class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    if (i, j) not in seen:
                        count += self.findIslands(i, j, grid, seen)
        return count
    
    def findIslands(self, row, col, grid, seen):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        if min(row, col) < 0 or row > max_row or col > max_col or (row, col) in seen or grid[row][col] == "0" :
            return 0
        seen.add((row, col))
        self.findIslands(row - 1, col, grid, seen)
        self.findIslands(row + 1, col, grid, seen)
        self.findIslands(row, col - 1, grid, seen)
        self.findIslands(row, col + 1, grid, seen)

        return 1
