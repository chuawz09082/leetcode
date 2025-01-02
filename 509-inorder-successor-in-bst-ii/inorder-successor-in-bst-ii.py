"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        """
        Finds the in-order successor of a given node in a binary tree.
        The in-order successor of a node is the smallest node value greater than the given node.
        
        @param node: The target node for which the successor needs to be found.
        @return: The in-order successor node, or None if no successor exists.
        """
        
        def dfs(root, visited, successor):
            """
            Performs a depth-first search to find the in-order successor.

            @param root: The current node being visited.
            @param visited: A set of node values already visited to prevent cycles.
            @param successor: The smallest value greater than the target node's value found so far.
            @return: The value of the in-order successor or the current smallest value.
            """
            # Base case: If the node is null or already visited, return the current successor.
            if not root or root.val in visited:
                return successor
            
            # Mark the current node as visited.
            visited.add(root.val)

            # Update successor if the current node's value is greater than the target node's value.
            if root.val - node.val > 0:
                successor = min(successor, root.val)

            # Traverse the left subtree if it contains potential successors.
            if root.left and root.left.val > node.val:
                left = dfs(root.left, visited, successor)
            else:
                left = float('inf')  # No valid successor in the left subtree.

            # Traverse the parent node.
            parent = dfs(root.parent, visited, successor)

            # Traverse the right subtree.
            right = dfs(root.right, visited, successor)

            # Return the minimum value among the potential successors.
            return min(min(parent, right), left)

        # Check if the in-order successor exists and return the corresponding Node.
        # Use `float('inf')` as a sentinel value to denote no successor.
        if dfs(node, set(), float('inf')) < float('inf'):
            # Create a new Node instance for the in-order successor.
            return Node(dfs(node, set(), float('inf')))
        
        # If no successor exists, return None.
        return None


        
