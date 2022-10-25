class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        hashmap = defaultdict(int)
        
        for item in nums:
            hashmap[item] += 1
        
        heap = [(-val, key) for key, val in hashmap.items()]
        heapq.heapify(heap)
        print(heap)
        out = []
        
        for i in range(k):
            item = heapq.heappop(heap)
            item = item[1]
            out.append(item)
        return out
