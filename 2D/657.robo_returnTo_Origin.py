class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hashMap = {
                      'U':0,
                      'D':0,
                      'L':0,
                      'R':0
                  }
        
        for move in moves:
            if move == 'U':
                if hashMap['D'] > 0:
                    hashMap['D'] -= 1
                else:
                    hashMap['U'] += 1
            elif move == 'D':
                if hashMap['U'] > 0:
                    hashMap['U'] -= 1
                else:
                    hashMap['D'] += 1
            elif move == 'L':
                if hashMap['R'] > 0:
                    hashMap['R'] -= 1
                else:
                    hashMap['L'] += 1
            elif move == 'R':
                if hashMap['L'] > 0:
                    hashMap['L'] -= 1
                else:
                    hashMap['R'] += 1
                    
        for key, val in hashMap.items():
            if val > 0:
                return False
        return True
