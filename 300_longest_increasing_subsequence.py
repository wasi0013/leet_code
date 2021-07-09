class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []
        for n in nums:
            i = bisect.bisect_left(seq, n)
            seq[i:i+1] = [n]
        return len(seq)

