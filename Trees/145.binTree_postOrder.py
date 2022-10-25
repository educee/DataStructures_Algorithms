# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        out = []
        
        def _postOrderHelper(node, out):
            if not node:
                return None
            
            _postOrderHelper(node.left, out)
            _postOrderHelper(node.right, out)
            out.append(node.val)
            
            return out
        return _postOrderHelper(root, out)
