# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum path sum in a binary tree. A path can start and end at any node.
        
        :param root: The root of the binary tree
        :return: The maximum path sum
        """

        def max_path(node):
            """
            Computes the maximum path sum from the current node to any leaf node.
            - If the node is None, return 0.
            - If the node has no children, return the node's value if it is non-negative; otherwise, return 0.
            - For other cases, compute the node's value plus the maximum of the left and right child paths.

            :param node: Current tree node
            :return: Maximum path sum ending at the current node
            """
            if not node:  # Base case: if the node is None, return 0
                return 0
            if not node.left and not node.right:  # Leaf node case
                if node.val < 0:  # Negative values do not contribute to the path
                    return 0
                return node.val
            # Compute max path sum including the current node's value
            val = node.val + max(max_path(node.left), max_path(node.right))
            # If the path sum is negative, return 0 (ignore this path)
            if val < 0:
                return 0
            return val

        def count_path(node):
            """
            Computes the maximum path sum that passes through the current node (including left and right subtrees).
            - If the node is None, return 0.
            - If the node is a leaf, return the node's value.
            - Otherwise, add the node's value with the maximum path sums from the left and right children.

            :param node: Current tree node
            :return: Maximum path sum passing through the current node
            """
            if not node:  # Base case: if the node is None, return 0
                return 0
            if not node.left and not node.right:  # Leaf node case
                return node.val
            # Sum of the current node's value and max paths from its left and right subtrees
            return node.val + max_path(node.left) + max_path(node.right)

        def determine_max(node):
            """
            Recursively computes the global maximum path sum.
            - If the node is None, return negative infinity (no valid path).
            - If the node is a leaf, return the node's value.
            - Recursively determine the max path sum in the left and right subtrees.
            - The result for the current node is the maximum of:
              1. The max path sum in the left subtree
              2. The max path sum in the right subtree
              3. The maximum path sum passing through the current node (count_path)

            :param node: Current tree node
            :return: The maximum path sum found in the subtree rooted at the current node
            """
            if not node:  # Base case: if the node is None, return negative infinity
                return float('-inf')
            if not node.left and not node.right:  # Leaf node case
                return node.val
            # Recursively calculate the max path sum in the left and right subtrees
            left_path = determine_max(node.left)
            right_path = determine_max(node.right)
            # Calculate the maximum path sum for the current node
            result = max(max(left_path, right_path), count_path(node))
            return result

        # Call the helper function starting at the root
        return determine_max(root)


        