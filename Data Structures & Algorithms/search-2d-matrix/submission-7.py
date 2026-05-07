class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, col = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1 

        while top <= bot:
            row = (top + bot) // 2
            if matrix[row][0] > target:
                bot = row - 1 
            elif matrix[row][-1] < target:
                top = row + 1 
            else:
                break
        
        if not (top <= bot):
            return False
        
        l, r = 0, col - 1 

        while l <= r:
            middle = (l + r) // 2
            if matrix[row][middle] > target:
                r = middle - 1
            elif matrix[row][middle] < target:
                l = middle + 1 
            elif matrix[row][middle] == target:
                return True
        return False


