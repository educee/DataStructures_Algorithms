# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, out):
            if not node:
                return
            
            inorder(node.left, out)
            out.append(node.val)
            inorder(node.right, out)
            
            return out
    
        if not root:
            return None
        out = []
        return inorder(root, out)
