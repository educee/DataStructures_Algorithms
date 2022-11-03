# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def _rangeSumBST(node, low, high):
            if not node:
                return
            
            if node.val >= low and node.val <= high:
                self.out += node.val
                
            if node.val > low:
                _rangeSumBST(node.left, low, high)
                
            if node.val < high:
                _rangeSumBST(node.right, low, high)
         
        if not root:
            return None
        self.out = 0
        _rangeSumBST(root, low, high)
        
        return self.out
