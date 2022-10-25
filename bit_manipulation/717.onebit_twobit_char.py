class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag = 0
        i = 0
        while i < len(bits):
            if bits[i] == 0:
                flag = 0
                i += 1
            else:
                flag = 1
                i += 2
        if flag: return False
        else: return True
