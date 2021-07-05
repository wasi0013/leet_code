class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = dict([i, j] for i, j in zip(s, t))
        return t == "".join(d[i] for i in s) and len(d.values()) == len(set(d.values()))  

