class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ghost = []
        ghost = nums[:]
        ans = nums + ghost
        return ans
        