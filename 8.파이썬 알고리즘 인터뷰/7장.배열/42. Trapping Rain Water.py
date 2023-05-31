# stack을 이용
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack  = []
        for i in range(len(height)) :
            while stack and height[i]>=height[stack[-1]] :
                j = stack.pop()
                if len(stack) == 0 : break
                distance = i - stack[-1] - 1
                water = min(height[i],height[stack[-1]])-height[j]
                result += distance*water
            stack.append(i)
        return result
    
#투포인터