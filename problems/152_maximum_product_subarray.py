class Solution:
    def maxProduct(self, nums: List[int]) -> int:    
        ans , max_p, min_p = nums[0], 1, 1   
        for num in nums:            
            max_p, min_p = max(num, min_p*num, max_p* num), min(num, min_p*num, max_p*num)
            ans = max(ans, max_p)
        return ans
            
    
