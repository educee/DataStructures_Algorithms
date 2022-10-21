#Leetcode - 15
#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if (i>0 and nums[i] == nums[i-1]):
                continue
            l, r = i+1, len(nums)-1
            
            while l < r:
                addedSum = nums[i] + nums[l] + nums[r]
                
                if addedSum == 0:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while (nums[l] == nums[l-1] and (l < r)):
                           l += 1
                elif addedSum > 0:
                    r -= 1
                elif addedSum < 0:
                    l += 1
        return out
