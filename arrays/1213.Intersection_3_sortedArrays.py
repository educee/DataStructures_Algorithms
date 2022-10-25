class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        hashmap = {}
        
        for item in arr1:
            if item in hashmap.keys():
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        for item in arr2:
            if item in hashmap.keys():
                hashmap[item] += 1
            else:
                hashmap[item] = 1
        for item in arr3:
            if item in hashmap.keys():
                hashmap[item] += 1
            else:
                hashmap[item] = 1
                
        out = []
        
        for key, val in hashmap.items():
            if val == 3:
                out.append(key)
                
        return out
      
      #Will add solution with O(1) space
