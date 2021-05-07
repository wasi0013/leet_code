class Solution:
    def fizzBuzz(self, n: int) -> List[str]: return [~x%3//2*"Fizz"+~x%5//4*"Buzz"or str(x) for x in range(1, n+1)]
        
