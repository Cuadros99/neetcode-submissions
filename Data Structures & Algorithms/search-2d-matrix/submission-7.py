class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        up, down = 0,  m-1

        while up <= down:
            middle = (up+down)//2

            if matrix[middle][0] > target:
                down = middle - 1
            elif matrix[middle][-1] < target:
                up = middle + 1
            else:
                break

        if not (up <= down):
            return False
        
        row = (up + down) // 2


        l, r = 0, n-1

        while l <= r:
            middle = (l+r)//2
            
            if matrix[row][middle] < target:
                l = middle + 1
            elif matrix[row][middle] > target:
                r = middle - 1
            else:
                return True

        return False