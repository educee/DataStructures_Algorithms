class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        
        for idx, val in enumerate(nums):
            if val in hashmap.keys():
                return True
            hashmap[val] = True
        return False
