class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        lcs = 0
        for num in uniq:
            count = 1
            if num - 1 in uniq: continue
            while num + count in uniq: count += 1
            lcs = max(count, lcs)
        return lcs
