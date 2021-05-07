class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "M" : 1000,
            "CM": 900 ,
            "D" : 500 ,
            "CD": 400 ,
            "C" : 100 ,
            "XC": 90  ,
            "L" : 50,
            "XL": 40,
            "X" : 10,
            "IX": 9,
            "V" : 5,
            "IV": 4,
            "I" : 1
            }
        
        l = len(s)
        num = 0
        i = 0
        while i< l:
            if i+1 < l and s[i:i+2] in mapping: 
                num += mapping[s[i:i+2]]
                i+=2
            else:
                num += mapping[s[i]]
                i += 1
        return num
            
            
            
        
