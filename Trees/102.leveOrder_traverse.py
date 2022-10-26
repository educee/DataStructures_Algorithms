# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        q = [root]
        out = []
        while q:
            levelLen = len(q)
            levelNodes = []
            for i in range(levelLen):
                curNode = q.pop(0)
                levelNodes.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            out.append(levelNodes)
            
        return out
            
