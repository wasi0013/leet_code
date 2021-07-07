from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter = Counter(chars)
        return sum(len(word)  for word in words if not any(word.count(c) > counter[c] for c in set(word)))

