# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def buildset(node, nodes):
            if not node:
                return
            nodes.add(node.val)
            buildset(node.left, nodes)
            buildset(node.right, nodes)
            
        def verifysum(node, nodes, target):
            if not node:
                return 
            if (target - node.val) in nodes:
                return True
            return verifysum(node.left, nodes, target) or verifysum(node.right, nodes, target)
            return False
            
            
        nodes = set()
        
        buildset(root1, nodes)
        
        return verifysum(root2, nodes, target)
