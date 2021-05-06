from itertools import chain
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]: return chain.from_iterable(zip(nums[:n],nums[n:]))
        
