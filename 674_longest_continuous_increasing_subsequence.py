class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        seek = nums[0]
        results = set([1])
        for i in nums[1::]:
            if i > seek:
                count += 1
            else:
                results.add(count)
                count = 1
            seek = i
        results.add(count)
        return max(results)
                
