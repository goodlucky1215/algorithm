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
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        result = 0
        left, right = 0,len(height)-1
        left_max, right_max = height[0], height[-1]
        while left < right:
            left_max, right_max = max(left_max,height[left]), max(right_max,height[right])
            if left_max<=right_max:
                result += left_max-height[left]
                left+=1
            else:
                result += right_max-height[right]
                right-=1
        return result