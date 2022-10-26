class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashmap = collections.defaultdict(int)
        out = []
        for item in items1:
            value, weight = item
            hashmap[value] += weight
            
        for item in items2:
            value, weight = item
            hashmap[value] += weight
        
        for key, val in hashmap.items():
            out.append([key, val])
        out.sort(key=lambda x: x[0])
        return out
        
