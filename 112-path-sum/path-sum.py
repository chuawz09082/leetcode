# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If the tree is empty, there can be no path, so return False
        if not root:
            return False

        # Helper function to perform depth-first search to check path sums
        def dfs(node: Optional[TreeNode], num: int) -> bool:
            # Check if we've reached a leaf node
            if not node.left and not node.right:
                # Return True if the sum of the path equals targetSum, otherwise False
                return num + node.val == targetSum
            # Recursively check the left and right subtrees with the updated sum
            # Return True if any path matches the target sum
            return (dfs(node.left, num + node.val) if node.left else False) or \
                   (dfs(node.right, num + node.val) if node.right else False)
        
        # Start the DFS from the root with an initial sum of 0
        return dfs(root, 0)
            
        
        