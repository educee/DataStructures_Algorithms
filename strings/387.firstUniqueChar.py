class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import OrderedDict
        
        hashmap = OrderedDict()
        
        for idx, c in enumerate(s):
            if c in hashmap.keys():
                hashmap[c][1] += 1
            else:
                hashmap[c] = [idx, 1]
            
        for key, val in hashmap.items():
            idx, count = val
            if count == 1:
                return idx
        return -1
