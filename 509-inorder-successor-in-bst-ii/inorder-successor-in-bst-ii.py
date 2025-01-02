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
        Finds the in-order successor of a node in a Binary Search Tree.
        
        @param node: The target node whose in-order successor is to be found.
        @return: The in-order successor node, or None if no successor exists.
        """
        # Case 1: Node has a right subtree
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left  # Find the leftmost node in the right subtree
            return successor
        
        # Case 2: Node does not have a right subtree
        current = node
        while current.parent and current.parent.right == current:
            current = current.parent  # Move up until we find a parent larger than the current node
        
        return current.parent  # The parent is the in-order successor, or None if no successor exists


        
