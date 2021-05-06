class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:    return sum(nums[i] == nums[j] for i in range(len(nums)-1) for j in range(i+1, len(nums)))
                    
                
        
