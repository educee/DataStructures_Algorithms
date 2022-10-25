class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import defaultdict
        hashmap = defaultdict(int)
        
        for num in arr:
            hashmap[num] += 1
        occurrences = set(hashmap.values())   
        
        return len(hashmap) == len(occurrences)
