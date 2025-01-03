# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Returns the number of nodes in the binary tree where the value of the node
        is equal to the average of the values in its subtree.

        @param root: The root of the binary tree.
        @return: The count of nodes satisfying the condition.
        """

        def dfs(node: TreeNode):
            """
            Performs a depth-first search (DFS) to calculate the sum, count of nodes, 
            and number of qualifying nodes for the subtree rooted at the given node.

            @param node: The current node being processed.
            @return: A tuple (subtree_sum, subtree_count, qualifying_nodes) where:
                     - subtree_sum: The sum of values in the subtree.
                     - subtree_count: The number of nodes in the subtree.
                     - qualifying_nodes: The count of nodes satisfying the condition.
            """
            if not node:
                # Base case: If the node is None, return zeros for all values.
                return 0, 0, 0
            
            if not node.left and not node.right:
                # Base case for leaf nodes:
                # The sum and count are the node's value and 1, respectively.
                # Leaf nodes always qualify since they are their own average.
                return node.val, 1, 1
            
            # Recursively process the left and right subtrees.
            leftsum, leftcount, leftnodes = dfs(node.left)
            rightsum, rightcount, rightnodes = dfs(node.right)

            # Calculate the total sum and count for the current subtree.
            total_sum = leftsum + rightsum + node.val
            total_count = leftcount + rightcount + 1

            # Check if the current node's value matches the average of its subtree.
            if node.val == total_sum // total_count:
                # If it matches, include this node in the count of qualifying nodes.
                return total_sum, total_count, leftnodes + rightnodes + 1
            else:
                # Otherwise, return the count without including this node.
                return total_sum, total_count, leftnodes + rightnodes

        # Call the DFS function starting from the root node.
        totalsum, totalcount, totalnodes = dfs(root)

        # Return the total count of qualifying nodes in the tree.
        return totalnodes
            

        