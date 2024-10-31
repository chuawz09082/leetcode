# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # If the root is None, return an empty list (no tree to print)
        if not root:
            return []
        
        # Initialize a queue with the root node, its level (1), and position (1) within its level
        queue = [(root, 1, 1)]
        
        # Track the current level of the tree and initialize `rootvals` with the root node's value and position
        currentlevel = 1
        rootvals = [(root.val, 1, 1)]

        # Level-order traversal to gather all nodes with their levels and positions
        while queue:
            nextlevel = []  # List to hold the next level of nodes
            for item in queue:
                current, level, pos = item[0], item[1], item[2]
                
                # If there's a left child, add it to the next level and update rootvals with its value and position
                if current.left:
                    nextlevel.append((current.left, level + 1, 2 * pos - 1))
                    rootvals.append((current.left.val, level + 1, 2 * pos - 1))
                
                # If there's a right child, add it to the next level and update rootvals with its value and position
                if current.right:
                    nextlevel.append((current.right, level + 1, 2 * pos))
                    rootvals.append((current.right.val, level + 1, 2 * pos))
            
            # Update the current level if there are nodes in the next level
            if nextlevel:
                currentlevel += 1
            queue = nextlevel  # Move to the next level

        # Calculate the dimensions of the final output grid
        rows = currentlevel
        cols = 2 ** currentlevel - 1  # Total columns needed for the last level's width

        # Initialize the grid with empty strings
        tree = [["" for _ in range(cols)] for _ in range(rows)]
        
        # Place each node's value at its calculated position in the grid
        for val, level, pos in rootvals:
            row = level - 1
            col = (2 ** (currentlevel - level) - 1) + (pos - 1) * (2 ** (currentlevel - level + 1))
            tree[row][col] = str(val)  # Convert the node's value to a string for placement in the grid

        # Return the grid representing the tree with each node positioned at its correct spot
        return tree

        
