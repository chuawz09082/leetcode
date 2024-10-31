"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base case: if root is None or it's a leaf node (no children), return the root
        if not root or (not root.left and not root.right):
            return root

        # Initialize stack to keep track of nodes at the current level, starting with the root node
        stack = [root]
        
        # `current` keeps track of the node to set `next` pointers for, starting with the root
        current = root
        
        # `node` is used to track the leftmost node of the next level
        node = current.left
         
        # Process each level until there are no more levels to traverse
        while stack:
            # `nextlevel` list to hold nodes at the next level
            nextlevel = []
            
            # Traverse each node in the current level stack
            for tree in stack:
                # If the current node has children, add them to `nextlevel`
                if tree.left:
                    nextlevel.append(tree.left)
                    nextlevel.append(tree.right)
            
            # Connect nodes horizontally in the current level
            for i in range(1, len(stack)):
                # Set `next` of the `current` node to the next node in the list
                current.next = stack[i]
                
                # Move `current` to the next node in the same level
                current = current.next
            
            # Reset `current` to `node`, which is the leftmost node of the next level
            current = node
            
            # Update `node` to the left child of the current `node` for the next level
            if node.left:
                node = node.left
            
            # Set `stack` to `nextlevel` to process the next level in the next iteration
            stack = nextlevel

        # Return the modified tree with connected `next` pointers
        return root
            


        