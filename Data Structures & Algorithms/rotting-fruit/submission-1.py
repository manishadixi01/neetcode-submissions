class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        total_time = 0
        seen = set()
        queue = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2 and (i,j) not in seen:
                    queue.append((i,j))
                    seen.add((i,j))
                if grid[i][j] == 1 and (i,j) not in seen:
                    fresh += 1
        while fresh > 0 and queue:
            queue_size = len(queue)
            for _ in range(queue_size):
                r, c = queue.pop(0)
                for dr, dc in directions:
                    ro, co = r + dr, c + dc
                    if ro in range(rows) and co in range(cols) and grid[ro][co] == 1 and (ro, co) not in seen:
                        queue.append((ro, co))
                        fresh -= 1
                    seen.add((ro, co))

            total_time += 1
        return total_time if fresh == 0 else -1





        

