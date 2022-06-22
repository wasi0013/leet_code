from string import ascii_lowercase
class Solution:
    def firstUniqChar(self, s: str) -> int:
        uniq_indexes = [s.index(c) for c in ascii_lowercase if s.count(c) == 1] 
        return min(uniq_indexes, default=-1)
            
