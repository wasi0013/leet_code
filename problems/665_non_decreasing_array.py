class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        change_needed = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if change_needed:
                    return False
                change_needed = True
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True


