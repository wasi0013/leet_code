from string import ascii_letters
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [i.lower() for i in s if i in ascii_letters or i in "0123456789"]
        return s == list(reversed(s))
