class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        r = n = len(seats)
        lp, rp = None, None
        res = [float("+inf")] * n
        for i in range(n):
            r -= 1
            left = seats[i]
            if left:
                lp = i
                res[i] = 0
            else: 
                if lp!=None:
                    res[i] = min(res[i], i-lp)    
            right = seats[r]
            if right:
                rp = r
                res[r] = 0
            else:
                if rp!=None:
                    res[r] = min(res[r], rp-r)
        return max(res)

