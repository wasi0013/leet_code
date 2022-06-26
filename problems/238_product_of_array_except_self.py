class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod, suffix_prod = 1, 1
        
        answer = [1] * n
        
        for i in range(n):
            answer[i] *= prefix_prod
            answer[-i-1] *= suffix_prod
            
            prefix_prod *= nums[i]
            suffix_prod *= nums[-i -1]
            
        return answer
