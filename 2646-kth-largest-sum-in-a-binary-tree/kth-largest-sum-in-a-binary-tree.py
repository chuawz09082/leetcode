# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th largest level sum in a binary tree.
        
        @param root: The root node of the binary tree.
        @param k: The target rank for the level sum.
        @return: The k-th largest level sum, or -1 if k exceeds the number of levels.
        """
        levelsum = []  # List to store the sum of node values for each level.
        current = [root]  # Initialize the current level with the root node.

        # Traverse the tree level by level.
        while current:
            nxtlevel = []  # List to store nodes for the next level.
            currentsum = 0  # Variable to store the sum of the current level.

            # Iterate through all nodes in the current level.
            for node in current:
                currentsum += node.val  # Add the node's value to the current level sum.
                # Add left and right children to the next level, if they exist.
                if node.left:
                    nxtlevel.append(node.left)
                if node.right:
                    nxtlevel.append(node.right)

            # Append the sum of the current level to the `levelsum` list.
            levelsum.append(currentsum)
            # Move to the next level.
            current = nxtlevel

        # If the total number of levels is less than k, return -1.
        if len(levelsum) < k:
            return -1

        # Sort the level sums in descending order.
        levelsum = sorted(levelsum, reverse=True)
        # Return the k-th largest level sum (1-indexed).
        return levelsum[k-1]
        