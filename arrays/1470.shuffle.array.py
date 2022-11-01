class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid = len(nums)//2
        out = []
        try:
            for i in range(mid):
                out.append(nums[i])
                out.append(nums[i+mid])
        except IndexError:
            pass
        
        return out
