class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        j1 = ''
        j2 = ''
        for word in word1:
            j1 += word
        for word in word2:
            j2 += word
            
        return j1 == j2
