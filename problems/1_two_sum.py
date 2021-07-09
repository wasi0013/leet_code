class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s_nums = sorted(nums)
        l = len(nums)
        for i, num in enumerate(nums):
            t = target - num
            o = bisect.bisect_left(s_nums, t)
            if o <l:
                if t == s_nums[o]:
                    try:
                        return i, nums.index(t,i+1)
                    except:
                        pass
        
