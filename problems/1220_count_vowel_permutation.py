class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        dp = [[0]*(n+1) for i in range(5)]
        for i in [0, 1, 2, 3, 4]: dp[i][1] = 1
        
        for i in range(2, n+1):
            dp[0][i] = (dp[1][i-1] + dp[2][i-1] + dp[4][i-1])% 1000000007
            dp[1][i] = (dp[0][i-1] + dp[2][i-1])% 1000000007
            dp[2][i] = (dp[1][i-1] + dp[3][i-1])% 1000000007
            dp[3][i] = (dp[2][i-1])% 1000000007
            dp[4][i] = (dp[2][i-1] + dp[3][i-1])% 1000000007
        
        return (dp[0][n]+dp[1][n]+dp[2][n]+dp[3][n]+dp[4][n])% 1000000007
