# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        # Helper function to validate if a subtree is a BST and return its properties
        def is_valid_Subtree(node: Optional[TreeNode]) -> (bool, int, int, int):
            # Base case: if the node is None, it's a valid BST with 0 nodes
            if not node:
                return True, 0, float('inf'), -float('inf')
            
            # Recursively validate the left subtree
            left_BST, left_count, left_min, left_max = is_valid_Subtree(node.left)
            # Recursively validate the right subtree
            right_BST, right_count, right_min, right_max = is_valid_Subtree(node.right)

            # Check if the current subtree is a valid BST:
            # - Both left and right subtrees must be BSTs
            # - The current node's value must be greater than the max value in the left subtree
            #   and less than the min value in the right subtree
            if left_BST and right_BST and left_max < node.val < right_min:
                # Calculate the total number of nodes in the current BST
                node_count = left_count + right_count + 1
                # Return True for valid BST, the node count, the min value in the subtree,
                # and the max value in the subtree
                return True, node_count, min(node.val, left_min), max(node.val, right_max)
            
            # If not a valid BST, return the larger count of nodes between the left and right subtrees
            # The min and max values are irrelevant in this case
            return False, max(left_count, right_count), 0, 0
        
        # Return the size of the largest BST subtree
        return is_valid_Subtree(root)[1]

            




