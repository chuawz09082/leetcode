# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Function to perform an inorder traversal on a binary tree
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result of the traversal
        res = []
        # Call the helper function to perform the DFS traversal
        self.dfs(root, res)
        # Return the list containing the inorder traversal result
        return res

    # Helper function to perform recursive DFS for inorder traversal
    def dfs(self, node: Optional[TreeNode], res: List[int]) -> None:
        # If the node is not null, continue the traversal
        if node:
            # Recursively traverse the left subtree
            self.dfs(node.left, res)
            # Append the current node's value to the result list
            res.append(node.val)
            # Recursively traverse the right subtree
            self.dfs(node.right, res)
        