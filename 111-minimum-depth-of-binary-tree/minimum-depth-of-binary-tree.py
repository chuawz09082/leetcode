# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        current = [root]
        depth = 1

        while current:
            nxtlevel = []
            for node in current:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    nxtlevel.append(node.left)
                if node.right:
                    nxtlevel.append(node.right)
            depth += 1
            current = nxtlevel
        
        