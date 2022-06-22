from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(sum(group) for _, group in groupby(nums))
