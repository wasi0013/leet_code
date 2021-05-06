class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            freq, val = nums[i:i+2]
            for n in range(freq):
                result.append(val)
        return result
