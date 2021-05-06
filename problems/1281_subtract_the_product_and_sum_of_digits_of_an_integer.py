class Solution:
    def subtractProductAndSum(self, n: int) -> int: 
        s, p = 0, 1
        while n:
            n, d = divmod(n, 10)
            s+=d
            p*=d
        return p - s
        
