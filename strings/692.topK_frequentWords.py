class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        
        hashmap = defaultdict(int)
        
        for word in words:
            hashmap[word] += 1
            
        return sorted(hashmap.keys(), key= lambda w: [-hashmap[w], w])[:k]
