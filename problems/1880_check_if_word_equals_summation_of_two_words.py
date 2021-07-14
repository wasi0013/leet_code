class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def convert(string):
            return int(''.join(str('abcdefghijklmnopqrstuvwxyz'.index(i)) for i in string))
        return  convert(firstWord)+convert(secondWord) == convert(targetWord)
        
