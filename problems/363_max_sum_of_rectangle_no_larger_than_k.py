class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def max_sub(array):
            max_sum = float('-inf')
            prefix_sum = 0
            prefix_sums = [float('inf')]
            for i in array:
                bisect.insort(prefix_sums, prefix_sum)
                prefix_sum += i
                t = bisect.bisect_left(prefix_sums, prefix_sum - k)
                max_sum = max(max_sum, prefix_sum - prefix_sums[t])
            return max_sum
            
        m  = len(matrix)
        n = len(matrix[0])
        ans = float("-inf")
        for row in range(n):
            col_sum = [0] * m
            for r in range(row, n):
                for col in range(0, m):
                    col_sum[col] += matrix[col][r]
                temp = max(ans, max_sub(col_sum))
                if temp < k:
                    ans = temp
                if temp == k:
                    return temp
        
        return ans
