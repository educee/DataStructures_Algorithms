class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        newarr = arr.copy()
        
        newarr.sort()
        
        hashmap = {}
        rank = 1
        for idx, num in enumerate(newarr):
            if num not in hashmap.keys():
                hashmap[num] = rank
                rank += 1
        
        out = [0]*len(arr)        
        for idx, num in enumerate(arr):
            out[idx] = hashmap[num]
            
            
        return out
