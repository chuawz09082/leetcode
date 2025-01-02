# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary search tree (BST) from its preorder traversal.

        @param preorder: List[int] - A list of integers representing the preorder traversal of a BST.
        @return: TreeNode - The root of the constructed BST.
        """
        # Base case: If the preorder list is empty, return None (no tree to construct).
        if not preorder:
            return None

        # Base case: If the preorder list contains only one element, create a single-node tree.
        if len(preorder) == 1:
            return TreeNode(preorder.pop())  # Pop the only element to create the node.

        # Step 1: The first element of the preorder list is the root of the current subtree.
        root_val = preorder.pop(0)  # Remove the root value from the list.
        root = TreeNode(root_val)  # Create the root TreeNode.

        # Step 2: Use bisect to find the index where the values greater than the root value begin.
        # All values before `root_index` belong to the left subtree, and values after belong to the right subtree.
        root_index = bisect.bisect_left(preorder, root_val)

        # Step 3: Recursively construct the left subtree using values before `root_index`.
        root.left = self.bstFromPreorder(preorder[:root_index])

        # Step 4: Recursively construct the right subtree using values after `root_index`.
        root.right = self.bstFromPreorder(preorder[root_index:])

        # Step 5: Return the constructed root node.
        return root
        