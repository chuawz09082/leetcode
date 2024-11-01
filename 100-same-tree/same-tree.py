# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base case: If both nodes are None, the trees are identical at this level
        if not p and not q:
            return True
        
        # If one node is None and the other is not, the trees are different
        elif not p or not q:
            return False
        
        # Recursive case:
        # 1. Check if current nodes' values are the same
        # 2. Recursively check if left subtrees are identical
        # 3. Recursively check if right subtrees are identical
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)