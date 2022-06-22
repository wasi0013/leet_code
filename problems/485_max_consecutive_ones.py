from itertools import groupby
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max(map(lambda item: sum(item[1]) * item[0], groupby(nums)))

