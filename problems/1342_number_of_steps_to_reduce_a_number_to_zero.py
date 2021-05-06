class Solution:
    def numberOfSteps(self, num: int, steps = 0) -> int: return steps if not num else self.numberOfSteps(num//2, steps+1) if num%2==0 else self.numberOfSteps(num-1, steps+1)
