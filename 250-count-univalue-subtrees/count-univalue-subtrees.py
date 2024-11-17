# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def is_unival_subtree(node: Optional[TreeNode]) -> bool:
            nonlocal count

            # A null node is trivially a unival subtree
            if not node:
                return True

            # Recursively check the left and right subtrees
            left_is_unival = is_unival_subtree(node.left)
            right_is_unival = is_unival_subtree(node.right)

            # Check if the current node forms a unival subtree
            if (
                left_is_unival
                and right_is_unival
                and (not node.left or node.left.val == node.val)
                and (not node.right or node.right.val == node.val)
            ):
                count += 1
                return True

            return False

        # Initialize the counter
        count = 0

        # Perform a bottom-up traversal to count unival subtrees
        is_unival_subtree(root)

        return count