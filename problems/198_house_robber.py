class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+2)
        for i in range(0, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]

