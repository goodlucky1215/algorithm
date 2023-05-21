class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums);
        nums_index = sorted(range(nums_len), key= lambda k: nums[k])
        frist, second = 0,1
        while():
            target_find = nums[nums_index[frist]]+nums[nums_index[second]];
