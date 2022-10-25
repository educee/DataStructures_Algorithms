class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = {}
        
        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        outLen = 0
        for num in nums:
            curOut = hashmap[num]
            if num-1 in hashmap.keys():
                curOut += hashmap[num-1]
                if curOut > outLen:
                    outLen = curOut
                    
        return outLen
