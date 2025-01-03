# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Prunes a binary tree such that subtrees not containing the value 1 are removed.
        
        @param root: The root of the binary tree.
        @return: The root of the pruned binary tree or None if the entire tree is pruned.
        """

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """
            Performs a post-order traversal to prune the tree.

            @param node: The current node being processed.
            @return: The node itself if it or its subtree contains the value 1, otherwise None.
            """
            # Base case: If the node is None, return None.
            if not node:
                return None
            
            # Leaf node case: If the node is a leaf and its value is not 1, prune it.
            if not node.left and not node.right:
                if node.val != 1:
                    return None  # Prune the node.
                else:
                    return node  # Keep the node if its value is 1.
            
            # Recursively prune the left and right subtrees.
            left = dfs(node.left)
            right = dfs(node.right)

            # If both left and right subtrees are pruned and the current node's value is not 1, prune it.
            if not left and not right:
                if node.val != 1:
                    return None
            
            # Update the node's left and right children after pruning.
            node.left = left
            node.right = right

            # Return the current node (either pruned or intact).
            return node
        
        # Start the pruning process from the root.
        return dfs(root)

        