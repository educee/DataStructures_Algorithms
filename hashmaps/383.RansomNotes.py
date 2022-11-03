class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = collections.Counter(magazine)
        print(hashmap)
        for c in ransomNote:
            if c not in hashmap.keys():
                
                return False
            else:
                hashmap[c] -= 1
                if hashmap[c] == 0:
                    del hashmap[c]
            
        return True
