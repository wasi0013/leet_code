class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:  
        
        def process_bit(bit, ans): 
            return not ans if bit else True
       
        return reduce(process_bit, bits[:-1:], True) 

