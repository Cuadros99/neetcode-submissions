class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        l, r = 0, m-1

        while r > l and r-l>1:
            middle = (r-l)//2 + l

            if matrix[middle][0] < target:
                l = middle
            elif matrix[middle][0] > target:
                r = middle-1
            else:
                return True
        
        i = l if matrix[r][0] > target else r
        l, r = 0, n-1

        while r >= l :
            middle = (r-l)//2 + l

            if matrix[i][middle] < target:
                l = middle + 1
            elif matrix[i][middle] > target:
                r = middle - 1
            else:
                return True
        
        return False
        

