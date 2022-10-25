# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def _preOrder(node, output):
            if not node:
                return
            
            output.append(node.val)
            _preOrder(node.left, output)
            _preOrder(node.right, output)
            
            return output
        if not root:
            return None
        output = []
        
        return _preOrder(root, output)
