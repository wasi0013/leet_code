class Solution:
    def trailingZeroes(self, n: int) -> int:
        a, b = 0, 5
        while n >= b: a, b = a+n//b, b*5
        return a
       

