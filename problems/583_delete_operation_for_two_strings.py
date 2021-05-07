class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        lw1 = len(word1)
        lw2 = len(word2)
        
        memo = [[float("inf")]*lw2 for _ in range(lw1)]
        
        def dp(index1, index2):
            if index1 == lw1 and  index2 == lw2:
                return 0
            if index1 == lw1:
                return dp(index1, index2+1) + 1
            if index2 == lw2:
                return dp(index1+1, index2) + 1
            if memo[index1][index2] != float("inf"):
                return memo[index1][index2]
            
            nos = float("inf")
            if word1[index1] == word2[index2]:
                return min(nos, dp(index1+1, index2+1))
            
            nos = min(nos, dp(index1+1, index2)+1)
            nos = min(nos, dp(index1, index2+1)+1)
            
            memo[index1][index2] = nos
            return nos
        return dp(0, 0)
            
        
