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
        for index, num in enumerate(nums):
            su = target - num
            if su in nums[index+1:]:
                return [first, second]
        return None;