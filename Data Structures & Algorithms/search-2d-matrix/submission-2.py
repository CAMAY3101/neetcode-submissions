class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix) # 3
        COLS= len(matrix[0]) # 4

        left = 0
        right = (ROWS * COLS) - 1 # 11

        while left <= right:
            mid = (left + right) // 2 # 5 6 6 7
            r = mid // COLS # 1 1 1 1
            c = mid % COLS # 1 2 2 3

            # 15 > matrix[1][1] (11)
            # 15 > matrix[1][2] (12)
            # 15 > matrix[1][2] (12)
            # 15 > matrix[1][3] (12)
            if target > matrix[r][c]:
                left += 1 # 1 2 3
            
            # 15 < matrix[1][1] (11)
            elif target < matrix[r][c]:
                right -= 1 
            else:
                return True
        return False 

            
            
