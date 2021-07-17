class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even_sum = [0] * n
        odd_sum = [0] * n
        even_sum[0] = nums[0]
        for i in range(1, n):
            if i%2 ==0:
                even_sum[i] = even_sum[i-1] + nums[i]
                odd_sum[i] = odd_sum[i-1]
            else:
                odd_sum[i] = odd_sum[i-1] + nums[i]
                even_sum[i] = even_sum[i-1]
       
        prefix_e, prefix_o = 0, 0
        
        ans = 0
        
        for i in range(n):
            suffix_e = even_sum[n-1] - even_sum[i]
            suffix_o = odd_sum[n-1] - odd_sum[i]
            ans += (prefix_e + suffix_o == prefix_o + suffix_e)
            prefix_e = even_sum[i]
            prefix_o = odd_sum[i]
        return ans
    
