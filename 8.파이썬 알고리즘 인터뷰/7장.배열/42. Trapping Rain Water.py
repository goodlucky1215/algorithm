class Solution:
    def trap(self, height: List[int]) -> int:
        volum = 0
        stack  = []
        for i in range(len(height)) :
