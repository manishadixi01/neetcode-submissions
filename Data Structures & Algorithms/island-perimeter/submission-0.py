class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        sum = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    if (j < cols - 1) and grid[i][j+1] == 0:
                        sum+=1
                    if (i < rows - 1) and grid[i+1][j] == 0:
                        sum += 1
                    if j > 0 and grid[i][j-1] == 0:
                        sum += 1
                    if i > 0 and grid[i-1][j] == 0:
                        sum += 1
                    if i == 0:
                        sum += 1
                    if i == rows - 1:
                        sum += 1
                    if j == 0:
                        sum += 1
                    if j == cols - 1:
                        sum += 1
        return sum