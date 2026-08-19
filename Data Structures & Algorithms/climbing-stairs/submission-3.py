class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp

        return one
        
    # O(n)


    #   n = 1 -> 1
    #   n = 2 -> 2 
    #   n = 3 -> 3