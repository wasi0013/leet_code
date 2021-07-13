class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        l, r = 1, 1
        for i in range(n):
            ans[i] *= l
            ans[-i-1] *= r
            l *= nums[i]
            r *= nums[-i-1]
        return ans
    
