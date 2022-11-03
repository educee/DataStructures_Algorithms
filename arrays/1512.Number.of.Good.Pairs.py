class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap = collections.Counter(nums)
        
        out = 0
        
        for val in hashmap.values():
            curOut = (val*(val-1))//2
            out += curOut
            
        return out
