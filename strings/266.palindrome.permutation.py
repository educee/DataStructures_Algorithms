class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        hashmap = {}
        
        for c in s:
            if c in hashmap.keys():
                hashmap[c] += 1
            else:
                hashmap[c] = 1
                
        flag = 0
        
        for key, val in hashmap.items():
            if val%2 == 0:
                continue
            if val%2 == 1:
                if flag == 0:
                    flag = 1
                else:
                    return False
                
        return True
                
