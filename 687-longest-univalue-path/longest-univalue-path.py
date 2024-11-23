# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty or has only one node, the longest univalue path is 0
        if not root or (not root.left and not root.right):
            return 0

        # Helper function to calculate the longest path of the same value starting from a node
        def maxpath(node: Optional[TreeNode], nodeval: int, length: int) -> int:
            # If both left and right children have the same value as the node, calculate paths recursively
            if node.left and node.right and node.left.val == nodeval == node.right.val:
                return max(maxpath(node.left, nodeval, length + 1), maxpath(node.right, nodeval, length + 1))
            # If the left child has the same value as the node, continue the path recursively
            if node.left and node.left.val == nodeval:
                return maxpath(node.left, nodeval, length + 1)
            # If the right child has the same value as the node, continue the path recursively
            if node.right and node.right.val == nodeval:
                return maxpath(node.right, nodeval, length + 1)
            # Return the current length if no further path exists
            return length

        # Perform a level-order traversal to evaluate each node
        current = [root]  # Start with the root node
        maxpathlength = 0  # Variable to track the longest path found

        while current:
            nxtlevel = []  # List to store the next level of nodes
            for node in current:
                path = 0  # Variable to store the path length for the current node

                # If both children have the same value as the current node, calculate the path length
                if node.left and node.right and node.left.val == node.val == node.right.val:
                    path = maxpath(node.left, node.val, 1) + maxpath(node.right, node.val, 1)
                    # Update the maximum path length if the calculated path is longer
                    if path > maxpathlength:
                        maxpathlength = path

                # If the left child has the same value as the current node, calculate the left path
                if node.left:
                    nxtlevel.append(node.left)  # Add the left child to the next level
                    if node.left.val == node.val:
                        path = maxpath(node.left, node.val, 1)

                # If the right child has the same value as the current node, calculate the right path
                if node.right:
                    nxtlevel.append(node.right)  # Add the right child to the next level
                    if node.right.val == node.val:
                        path = maxpath(node.right, node.val, 1)

                # Update the maximum path length if the current path is longer
                if path > maxpathlength:
                    maxpathlength = path

            current = nxtlevel  # Move to the next level of nodes
        return maxpathlength  # Return the longest univalue path found
        