class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = [0]* n
        for i in range(n):
            a[i] = nums[nums[i]]
        return a
        
