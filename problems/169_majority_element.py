class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        s = dict()
        for i in nums:
            s[i] = s.get(i, 0) + 1
            if s[i] > n/2:
                return i


