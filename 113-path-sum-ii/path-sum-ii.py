# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        current = [[root,[root.val]]]
        result = []

        while current:
            nxtlevel = []
            for node,listvals in current:

                if not node.left and not node.right and sum(listvals) == targetSum:
                    result.append(listvals)
                if node.left:
                    nxtlevel.append([node.left,listvals + [node.left.val]])
                if node.right:
                    nxtlevel.append([node.right,listvals + [node.right.val]])
            current = nxtlevel
        
        return result
        
            

        