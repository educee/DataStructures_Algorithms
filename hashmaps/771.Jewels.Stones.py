class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashmap = collections.Counter(stones)
        
        out = 0
        
        for key in jewels:
            out += hashmap[key]
            
        return out
