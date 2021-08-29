from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return [i for i, j in c.items() if j == 1]
        
