class Solution:
    def thousandSeparator(self, n: int) -> str:
        
        return str(n) if n<=999 else ''.join('.'+x if (i%3==0 and i!=0) else x for i,x in enumerate(str(n)[::-1], 0))[::-1]
    
