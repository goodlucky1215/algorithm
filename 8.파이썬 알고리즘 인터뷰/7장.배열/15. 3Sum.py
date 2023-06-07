#브루트포스 : 타임아웃
import collections
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(0, len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, len(nums) - 1):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    if(nums[i] + nums[j] + nums[k])==0:
                        result.append([nums[i],nums[j],nums[k]])
        return result

#투 포인터
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(0, len(nums)-2):
            left, right = i+1,len(nums)-1
            if nums[i]>0: break
            if (i>0 and nums[i]==nums[i-1]) : continue
            while left<right:
                if nums[i]+nums[left]+nums[right]>0:
                    right-=1
                elif nums[i]+nums[left]+nums[right]<0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    right -= 1
                    left += 1
        return result
