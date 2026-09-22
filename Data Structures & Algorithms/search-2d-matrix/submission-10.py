class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # treat the matrix as a single sorted array of size rows X cols
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            row = mid // COLS
            cols = mid % COLS

            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return False      