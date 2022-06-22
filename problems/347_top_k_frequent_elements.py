from collections import Counter
from heapq import nlargest

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        return nlargest(k, n:=Counter(nums), key = lambda x: n[x]) 
        
