class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import defaultdict
        mydict = defaultdict(int)
        for c in s:
            mydict[c] += 1
        
        for c in t:
            if c in mydict.keys():
                mydict[c] -= 1
                if mydict[c] == 0:
                    del mydict[c]
            
        return sum(mydict.values())
