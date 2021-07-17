class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = ['a']*n
        k = k - n
        while k:
            if k >=25:
                ans[n-1] = "z"
                k -= 25
                n-=1
            else:
                ans[n-1] = chr(ord('a')+k)
                k = 0
        return "".join(ans)
        
        
        
