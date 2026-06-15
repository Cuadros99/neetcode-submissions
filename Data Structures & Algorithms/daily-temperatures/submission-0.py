class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0]*len(temperatures)
        
        for d, t in enumerate(temperatures):
            while len(stack) > 0 and t > stack[-1][0]:
                output[stack[-1][1]] = d - stack[-1][1]
                stack.pop()
            
            stack.append((t,d))

        return output