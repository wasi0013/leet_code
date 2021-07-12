class NumArray:

    def __init__(self, nums: List[int]):
        self.n = list(accumulate(nums))
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.n[right]- (self.n[left-1] if left>0 else 0)
        
