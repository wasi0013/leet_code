class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int: return sum(stones.count(c) for c in jewels)
        
