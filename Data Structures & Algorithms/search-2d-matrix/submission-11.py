class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten the array 
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l, r = 0, ROWS * COLS - 1

        while l <= r:
            mid = l + (r - l) // 2
            # convert the mid back to matrix coordinates
            rows, cols = mid // COLS, mid % COLS
            
            if target < matrix[rows][cols]:
                r = mid - 1
            elif target > matrix[rows][cols]:
                l = mid + 1
            else:
                return True
        
        return False 