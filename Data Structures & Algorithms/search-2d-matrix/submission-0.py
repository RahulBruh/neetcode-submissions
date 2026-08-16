class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0]) - 1
        ud = 0

        while l <= r:
            m = (l + r) // 2
            while target > matrix[ud][r]:
                ud += 1
                if ud > len(matrix) - 1:
                    return False
                    
            if matrix[ud][m] == target:
                return True
            
            elif target > matrix[ud][m]:
                l = m + 1
            
            else:
                r = m - 1

        return False    