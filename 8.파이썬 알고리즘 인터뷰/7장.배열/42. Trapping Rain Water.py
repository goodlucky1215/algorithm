class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0;
        start = 0
        stack = []
        for i in range(len(height)) :
            if height[i]!=0:
                stack.append[height[i]]
                start = i+1
                break
        if(len(height)==start) : return 0
        for i in height[start:]:
            if stack[-1]>i:
                stack.append(i)
            while stack[-1]<i:
                if len(stack)==1:
                    stack.pop();
                    stack.append(i)



