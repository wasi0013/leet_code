class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current_rung = 0
        count = 0
        for next_rung in rungs: 
            if current_rung + dist < next_rung:
                div, mod = divmod(next_rung - current_rung, dist)
                count += div - (mod == 0)
            current_rung = next_rung    
        return count
    
