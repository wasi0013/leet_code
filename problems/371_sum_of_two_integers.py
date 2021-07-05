class Solution:
    def getSum(self, a: int, b: int) -> int:
        a , b = max(a,b), min(a, b)
        while b & 0xffffffff != 0:
            c = a & b
            a = a ^ b
            b = c << 1
        return a & 0xffffffff if b > 0xffffffff else a
        
