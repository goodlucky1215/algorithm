#브루트포스 :
import collections
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                nums_add = nums[i]+nums[j]
                for k in range(j+1, len(nums)) :
                    if(nums_add + nums[k])==0:
                        lists = [nums[i],nums[j],nums[k]]
                        lists.sort()
                        result.add(tuple(lists))
        result_list = [list(t) for t in result]
        return result_list

