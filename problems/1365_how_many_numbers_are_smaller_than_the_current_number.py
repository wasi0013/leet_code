class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: return map(lambda x: sum(i<x for i in nums) , nums)
        
