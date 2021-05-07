class Solution:
    def countPrimes(self, n: int) -> int:
        s=[0,0]+list(range(2,n+1));b=2
        while b*b<n:s[2*b:n:b]=[0]*((n-1)//b-1);b+=1
        p=list(filter(None,s))
        return max(len(p)-1, 0)
