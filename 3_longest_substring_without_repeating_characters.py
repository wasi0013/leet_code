class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        result = 0
        for i in s:
            if i not in temp:
                temp.append(i)
            else:
                result = max(result, len(temp))
                temp = temp[temp.index(i)+1::]
                temp.append(i)
            print(temp)
        result = max(result, len(temp))
        return result
    
