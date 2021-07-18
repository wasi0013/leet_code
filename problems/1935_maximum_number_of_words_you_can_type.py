class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        broken_chars = set(brokenLetters)
        for word in text.split(" "):
            unique_chars = set(word)
            count += (len(unique_chars - broken_chars) == len(unique_chars))
        return count

