class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = m+n - 1
        while t>=0:
            if n>0:
                if m > 0:
                    if nums1[m-1] < nums2[n-1]:
                        nums1[t] = nums2[n-1] 
                        n -= 1
                    else:
                        nums1[t] = nums1[m-1]
                        m -= 1
                else:
                    nums1[t] = nums2[n-1] 
                    n -= 1
                    
            else:
                if m>0:
                        nums1[t] = nums1[m-1]
                        m -= 1
            t -= 1

