class KthLargest:
    k = None
    nums = []
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        i = bisect.bisect_left(self.nums, val)
        self.nums.insert(i, val)
        return self.nums[-self.k]
        

