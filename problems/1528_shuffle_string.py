class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str: return "".join(s[indices.index(n)] for n in range(len(s)))
