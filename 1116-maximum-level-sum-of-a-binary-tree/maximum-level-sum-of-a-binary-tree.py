# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, return 0 as there are no levels to evaluate
        if not root:
            return 0

        # Initialize variables to track the maximum sum and corresponding level
        maxlevel = 1  # Root level starts at 1
        maxsum = root.val  # Initialize maxsum as the value of the root node

        # Start BFS traversal with the root node
        current = [root]  # List to store nodes of the current level
        currentlvl = 2  # Start checking levels from level 2

        # Perform BFS to traverse the tree level by level
        while current:
            nxtlevel = []  # List to store nodes of the next level
            currentsum = 0  # Sum of node values for the current level
            added = False  # Flag to check if any nodes were added to the next level

            # Process all nodes in the current level
            for node in current:
                # If the node has a left child, add it to the next level
                if node.left:
                    nxtlevel.append(node.left)
                    # Add the left child's value to the current level's sum
                    currentsum += node.left.val
                    added = True  # Mark that a node was added
                
                # If the node has a right child, add it to the next level
                if node.right:
                    nxtlevel.append(node.right)
                    # Add the right child's value to the current level's sum
                    currentsum += node.right.val
                    added = True  # Mark that a node was added

            # Update the maximum level and sum if conditions are met:
            # - Nodes were added at the current level (`added` is True)
            # - The sum of the current level exceeds the recorded maximum sum
            if added and currentsum > maxsum:
                maxlevel = currentlvl  # Update the maximum level
                maxsum = currentsum  # Update the maximum sum
            
            # Move to the next level
            currentlvl += 1  # Increment the level counter
            current = nxtlevel  # Update the current level nodes for the next iteration

        # Return the level with the maximum sum
        return maxlevel
            

