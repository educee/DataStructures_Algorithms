class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        out = 0
        
        for i in range(len(accounts)):
            curMax = sum(accounts[i])
            if curMax > out:
                out = curMax
                
        return out
