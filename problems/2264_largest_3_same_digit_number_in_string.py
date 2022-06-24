from itertools import groupby
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_nums = [] 
        
        for _k, group in groupby(num): 
            s = ''.join(group)[:3]
            if len(s) == 3:
                good_nums.append(s)
                
        ans = str(max(good_nums, default=''))
        
        return "000" if ans == "0" else ans
