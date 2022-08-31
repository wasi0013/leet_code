from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def compare(elem):
            """compares first two elements a, b of an iterable & returns 0 if a == b, 1 if a > b and -1 if a < b"""
            a, b = int(elem[0]), int(elem[1])
            return [[0, 1][a > b], -1][a < b]
        for i in map(compare, zip_longest(version1.split("."), version2.split("."), fillvalue=0)):
            if i != 0: return i
        return 0

