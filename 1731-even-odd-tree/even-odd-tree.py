# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree satisfies the conditions of an Even-Odd Tree:
        1. Nodes on even-indexed levels must have strictly increasing odd values.
        2. Nodes on odd-indexed levels must have strictly decreasing even values.

        @param root: The root of the binary tree.
        @return: True if the tree satisfies the conditions, False otherwise.
        """

        # Initialize the current level with the root node.
        current = [root]
        # Track the current level index (0-based).
        lvl = 0

        # Perform a level-order traversal of the tree.
        while current:
            nxtlevel = []  # List to store the nodes for the next level.
            currentval = []  # List to store the values of nodes at the current level.

            # Iterate through all nodes in the current level.
            for node in current:
                # Even-indexed level conditions:
                if lvl % 2 == 0:
                    # The value must be odd and strictly increasing.
                    if (node.val % 2 == 0 or (currentval and currentval[-1] >= node.val)):
                        return False
                # Odd-indexed level conditions:
                else:
                    # The value must be even and strictly decreasing.
                    if (node.val % 2 == 1 or (currentval and currentval[-1] <= node.val)):
                        return False
                
                # Add the current node's value to the list for this level.
                currentval.append(node.val)

                # Add the left and right children to the next level (if they exist).
                if node.left:
                    nxtlevel.append(node.left)
                if node.right:
                    nxtlevel.append(node.right)
            
            # Move to the next level.
            current = nxtlevel
            # Increment the level index.
            lvl += 1
        
        # If all levels satisfy the conditions, return True.
        return True
                
        