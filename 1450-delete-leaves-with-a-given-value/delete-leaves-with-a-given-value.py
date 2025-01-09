# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Removes all leaf nodes in a binary tree that have the given target value. 
        If a node becomes a leaf node and has the target value after removing its children, it is also removed.

        @param root: Optional[TreeNode] - The root of the binary tree.
        @param target: int - The target value for leaf nodes to be removed.
        @return: Optional[TreeNode] - The updated tree with target-value leaf nodes removed.
        """

        def dfs(node):
            """
            Recursive helper function to traverse the tree and remove target-value leaf nodes.

            @param node: TreeNode - The current node being processed.
            @return: TreeNode - The updated node after processing its children.
            """
            if not node:
                # Base case: If the current node is None, return None.
                return None

            # Check if the current node is a leaf node.
            if not node.left and not node.right:
                # If the current node is a leaf and its value equals the target, remove it (return None).
                if node.val == target:
                    return None
                else:
                    # Otherwise, retain the node.
                    return node
            
            # Recursively process the left and right children.
            left = dfs(node.left)
            right = dfs(node.right)

            # If the current node becomes a leaf (both children are None) and its value equals the target, remove it.
            if node.val == target and not left and not right:
                return None

            # Update the node's children with the results of the recursive calls.
            node.left = left
            node.right = right

            # Return the current node after processing.
            return node
        
        # Start the DFS traversal from the root.
        return dfs(root)