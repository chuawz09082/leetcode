# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it is balanced by definition, so return True
        if not root:
            return True
        
        # Helper function to calculate the height of a given node
        def calculate_height(node: Optional[TreeNode]) -> int:
            # If the node is None, return height as 0
            if not node:
                return 0
            # Recursively calculate the height of the left and right subtrees,
            # and return the maximum height plus 1 (for the current node)
            return max(calculate_height(node.left), calculate_height(node.right)) + 1
        
        # Check the height difference between the left and right subtrees of the root
        # If the absolute difference in height is less than or equal to 1, check if both subtrees are balanced
        if abs(calculate_height(root.left) - calculate_height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            # If the height difference is within 1 and both subtrees are balanced, return True
            return True
        else:
            # If the height difference is greater than 1 or any subtree is not balanced, return False
            return False
        

        