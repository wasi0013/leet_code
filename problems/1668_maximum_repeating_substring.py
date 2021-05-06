class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int: 
        c = sequence.count(word)
        if not c: return 0
        for i in range(c, 0, -1):
            t = sequence.count(word*i)
            if t: return i
        
