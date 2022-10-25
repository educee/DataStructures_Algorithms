class Solution:
    from collections import defaultdict
    import random
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.hashmap = defaultdict(list)
        self.generatehashmap()
        
    def generatehashmap(self):
        for idx, item in enumerate(self.nums):
            self.hashmap[item].append(idx)
        

    def pick(self, target: int) -> int:
        l = self.hashmap[target]
        return random.choice(l)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
