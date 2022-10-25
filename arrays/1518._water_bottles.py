class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        out = numBottles
        
        q = numBottles
        
        while q:
            if q >= numExchange:
                div = q//numExchange
                rem = q%numExchange
                q = div + rem
                out += div
            else:
                break
        return out
                
