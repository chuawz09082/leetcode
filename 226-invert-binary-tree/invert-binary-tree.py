# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If the tree is empty, return None since there is nothing to invert
        if root is None:
            return 

        # Helper function to recursively swap the left and right children of each node
        def swap(node: Optional[TreeNode]) -> Optional[TreeNode]:
            # Base case: if the node is a leaf (no children), return the node as is
            if not node.left and not node.right:
                return node

            # Swap the left and right children of the current node
            tmpnode = node.left
            node.left = node.right
            node.right = tmpnode

            # Recursively apply the swap on the left and right subtrees
            # Check if there is a left child, and if so, recursively swap its children
            if node.left:
                node.left = swap(node.left)
            # Check if there is a right child, and if so, recursively swap its children
            if node.right:
                node.right = swap(node.right)

            # Return the current node after its children have been swapped
            return node

        # Call the swap function starting from the root node to invert the entire tree
        return swap(root)


        