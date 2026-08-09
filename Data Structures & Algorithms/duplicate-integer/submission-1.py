class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set(nums)
        s2 = len(s1)
        if s2 == len(nums):
            return False
        else:
            return True