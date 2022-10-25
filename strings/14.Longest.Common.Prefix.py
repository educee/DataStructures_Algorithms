class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = 0
        
        for chars in zip(*strs):
            
            if len(set(chars)) == 1:
                res += 1
            else:
                break
        
        return strs[0][:res]
