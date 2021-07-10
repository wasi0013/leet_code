class Solution:
    def maxArea(self, height: List[int]) -> int:
        m = len(height)
        area, i, j = 0, 0, m-1
        while i < j:
            h = min(height[i], height[j])
            area = max(area, h* (j-i))
            if height[i] == h:
                i += 1
            if height[j] == h:
                j -= 1
        return area
    
