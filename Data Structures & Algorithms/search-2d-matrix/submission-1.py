class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        for i in range(m + 1):
            if target <= matrix[i][n]:
                return self.binarySearch(target, matrix[i], 0, n)
        return False
    
    def binarySearch(self, target, row, l, r):
        while l <= r:
            mid = l + (r - l)//2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                l = mid + 1
            elif row[mid] > target:
                r = mid - 1
        return False
        




        