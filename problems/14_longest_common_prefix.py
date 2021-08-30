class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre, *sorted_strs = sorted(set(strs), key=lambda x: len(x))
        for i, c in enumerate(pre):
            for s in sorted_strs:
                if s[i] != c:
                    return pre[:i]
        return pre
            
