# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Constructs a binary tree from inorder and postorder traversal arrays.

        @param inorder: List[int] - Inorder traversal of the tree.
        @param postorder: List[int] - Postorder traversal of the tree.
        @return: TreeNode - The root of the constructed binary tree.
        """
        if not inorder or not postorder:
            return None

        # Step 1: The last element in the postorder list is the root of the tree.
        root_val = postorder.pop()
        root = TreeNode(root_val)

        # Step 2: Find the root's index in the inorder list.
        root_index = inorder.index(root_val)

        # Step 3: Recursively build the right subtree and left subtree.
        # Right subtree is built first because postorder traversal visits left -> right -> root.
        root.right = self.buildTree(inorder[root_index + 1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root      