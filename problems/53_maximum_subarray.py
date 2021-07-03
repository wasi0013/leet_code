class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum , temp_sum = float("-inf"), 0
        for i in nums:
            largest_sum = max(largest_sum, temp_sum + i)
            temp_sum = max(0, temp_sum + i)
        return largest_sum
