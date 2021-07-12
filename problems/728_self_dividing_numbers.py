
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]: 
        def is_sd(num):
            n = num
            while n > 0:
                n, m = divmod(n, 10)
                if m == 0:
                    return False
                if num % m != 0:
                    return False
            return True
        return [i for i in range(left, right+1) if is_sd(i)]
        
