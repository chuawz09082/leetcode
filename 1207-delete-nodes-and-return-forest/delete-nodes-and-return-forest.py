# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        """
        Deletes the nodes specified in the `to_delete` list and returns the resulting forest.

        @param root: The root of the binary tree.
        @param to_delete: List of node values to be deleted.
        @return: List of TreeNode objects representing the roots of the resulting forest.
        """
        result = []  # List to store the roots of the trees in the resulting forest.

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """
            Performs a depth-first search to traverse and modify the tree.

            @param node: Current node being processed.
            @return: The modified subtree rooted at this node, or None if the node is deleted.
            """
            if not node:  # Base case: If the node is None, return None.
                return None
            
            # If the current node is in the `to_delete` list, process its children.
            if node.val in to_delete:
                # If the left child exists, process it recursively.
                if node.left:
                    leftnode = dfs(node.left)
                    # If the left child is not deleted, add it to the result as a new root.
                    if leftnode:
                        result.append(leftnode)

                # If the right child exists, process it recursively.
                if node.right:
                    rightnode = dfs(node.right)
                    # If the right child is not deleted, add it to the result as a new root.
                    if rightnode:
                        result.append(rightnode)

                # Return None because the current node is deleted.
                return None

            # If the current node is a leaf node, simply return it.
            if not node.left and not node.right:
                return node

            # Recursively process the left and right children.
            left = dfs(node.left)
            right = dfs(node.right)

            # Return the current node with updated left and right children.
            return TreeNode(node.val, left, right)
        
        # Process the root node and check if it should be added to the result.
        newnode = dfs(root)
        if newnode:  # If the root is not deleted, add it to the result.
            result.append(newnode)
        
        return result  # Return the forest of trees.




