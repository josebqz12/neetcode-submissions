class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ghost = nums[:]
        ans = nums + ghost
        return ans
        