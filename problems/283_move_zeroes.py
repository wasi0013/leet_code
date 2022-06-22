class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indices = [i for i,j in enumerate(nums) if j==0]
        
        for i, j in enumerate(indices): nums.pop(j)
        
        nums = nums.extend([0]*len(indices))
        
