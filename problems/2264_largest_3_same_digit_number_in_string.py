from itertools import groupby
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = max([c for key, group in groupby(num) if len(c:=''.join(group)[:3]) >= 3], default='')
        return "000" if ans =="0" else ans
