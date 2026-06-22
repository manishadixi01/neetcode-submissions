class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        return self.matrixdfs(0, 0, grid, visited)

    def matrixdfs(self, row, col, grid, visited):
        max_row = len(grid) - 1
        max_col = len(grid[0]) - 1
        if min(row, col) < 0 or row > max_row or col > max_col or grid[row][col] == 1 or (row, col) in visited:
            return 0
        if (row == max_row and col == max_col):
            return 1
        
        visited.add((row, col))
        # print(f"status - row = {row}, col = {col}, visited so far = {visited}")
        count = 0
        count += self.matrixdfs(row - 1, col, grid, visited)
        count += self.matrixdfs(row + 1, col, grid, visited)
        count += self.matrixdfs(row, col + 1, grid, visited)
        count += self.matrixdfs(row, col - 1, grid, visited)
        visited.remove((row, col))

        return count
