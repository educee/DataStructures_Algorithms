# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        
        def _getLonelyNodes(node, out):
            if not node:
                return
            if not node.right and node.left:
                out.append(node.left.val)
            elif not node.left and node.right:
                out.append(node.right.val)
            
            _getLonelyNodes(node.left, out)
            _getLonelyNodes(node.right, out)
            
            return out
        
        return _getLonelyNodes(root, out)
