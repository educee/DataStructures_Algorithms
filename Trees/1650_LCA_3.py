"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        p_set = set()
        cur_p = p
        while cur_p:
            p_set.add(cur_p)
            cur_p = cur_p.parent
        
        cur_p = q
        while cur_p:
            if cur_p in p_set:
                return cur_p
            cur_p = cur_p.parent
        
        return None
