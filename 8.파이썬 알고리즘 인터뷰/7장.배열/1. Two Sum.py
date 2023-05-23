#브루트포스
class Solution:
    def twoSum1(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for first in nums_len-1:
            for second in range(first+1,nums_len):
                if(nums[first]+nums[second]==target) :
                    return [first, second]
        return None;

#브루트포스와 같은 시간복잡도로 같지만, if문에서 ==보다는 in이 빠르다.
class Solution:
    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for i, num in enumerate(nums):
            su = target - num
            if su in nums[i+1:]:
                return [i, nums[i+1:].index(su)+i+1]

#index와 값을 반대로 담아서 해결
class Solution:
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            dict[num] = i
        for i, num in enumerate(nums):
            if target-num in dict and i!=dict[target-num]:
                return [i,dict[target-num]]

#index와 값을 반대로 담아서 해결 : 히나의 포문으로 합침
class Solution:
    def twoSum3(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if target-num in dict and i!=dict[target-num]:
                return [i,dict[target-num]]
            dict[num] = i
