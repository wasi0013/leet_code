class Solution:
    def isHappy(self, n: int) -> bool:
        repeated = set()
        while n != 1:
            if n in repeated:
                return False
            else:
                repeated.add(n)
            n = sum([int(i)*int(i) for i in str(n)])
        return True

