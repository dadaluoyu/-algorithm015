#LC74
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
         
        m = len(matrix) - 1
        if m < 0:
            return False
        n = len(matrix[0]) - 1
        
        left, up = 0, 0
        right, down = n, m
        
        while left <= right and up <= down:
            
            i = (up + down) // 2
            j = (left + right) // 2
            #j = right
            
            #print(i, j)
            if matrix[i][j] == target:
                return True
            
            elif matrix[i][j] < target:
                    
                if j == n:    
                    up = i + 1
                    left = 0
                else:
                    left = j + 1
                
            elif matrix[i][j] > target:
                
                if j == 0:
                    down = i - 1
                    right = n
                else:
                    right = j - 1
                    
        return False
