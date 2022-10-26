class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        flag = 0
        l = 0
        while l < len(s):
            start = l
            end = min(l+k, len(s))
            revstr = s[l:l+k]
            s = s[:l] + revstr[::-1] + s[l+k:]
            print(s)
            l += 2*k
            
        return s
