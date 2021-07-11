class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        m = len(s)
        d = defaultdict(list)
        
        for i in range(m):
            d[s[i]].append(i)
        
        ans = 0
        for l in d.values():
            if len(l) > 1:
                ans+=len(set(s[l[0]+1:l[-1]]))
                
        return ans
                
        
