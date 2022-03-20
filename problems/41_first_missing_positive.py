 """ 41. First Missing Positive

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
 

Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
        
"""
    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        The solution must have to be o(n) and o(1)
        Need to find smallest missing positive integer. 
        So, The answer should be at least 1 and at max length + 1
        i.e. we can discard all the negative numbers & numbers greater than length + 1
        We could use a dict of freq of numbers but, that will require space. 
        So, instead we use the classic % based freq counter to store both the number and it's frequency.
        """
       
        
        nums.append(0)
        length = len(nums)
        
        for i in range(length):
            if nums[i] < 0 or nums[i] >= length:
                nums[i] = 0
        print(length, nums)
        
        for i in range(length):
            index = nums[i] % length
            nums[index] += length
        
        for num in range(1, length):
            if nums[num] // length == 0: 
                return num
        
        return length
