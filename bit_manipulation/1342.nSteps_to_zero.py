class Solution:
    def numberOfSteps(self, num: int) -> int:
        out = 0
        
        while num > 0:
            curRes = num//2
            if num%2 == 1:
                num = num-1
            else:
                num = curRes
            out += 1
        return out
    
    
#class Solution:
#    def numberOfSteps (self, num: int) -> int:
#        steps = num == 0
#        while num > 0:
#            steps += 1 + (num & 1)
#            num >>= 1
#        return steps - 1
