class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        left, right = [height[0]], [height[-1]]
        for i in range(1, len(height)):
            left.append(max(left[i - 1], height[i]))
            right.append(max(height[len(height) - i - 1], right[i - 1]))

        return sum(
            min(left[i], right[len(height) - 1 - i]) - height[i]
            for i in range(len(height))
        )
