class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        nums.sort()
        for i,num in enumerate(nums):
            if num == nums[i-1]:
                return True
        return False


        