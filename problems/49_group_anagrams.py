class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for string in strs:
            key = ''.join(sorted(string))
            if d.get(key): 
                d[key].append(string)
            else: 
                d[key] = [string]
        return list(d.values())

