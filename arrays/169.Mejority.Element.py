class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        hashmap = defaultdict(int)
        curMax = 0
        out = 0
        for item in nums:
            hashmap[item] += 1
            if hashmap[item] > curMax:
                curMax = hashmap[item]
                out = item
        return out
