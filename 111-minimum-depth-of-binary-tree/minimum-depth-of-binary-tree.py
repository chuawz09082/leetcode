# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the root is None (i.e., the tree is empty), return a depth of 0
        if not root:
            return 0
        
        # Initialize the current level with the root node and set the initial depth to 1
        current = [root]
        depth = 1

        # Perform a level-by-level traversal (BFS) until we find a leaf node
        while current:
            nxtlevel = []  # List to store nodes of the next level
            for node in current:
                # If the node is a leaf node (no left or right children), return the current depth
                if not node.left and not node.right:
                    return depth
                # If the node has a left child, add it to the next level
                if node.left:
                    nxtlevel.append(node.left)
                # If the node has a right child, add it to the next level
                if node.right:
                    nxtlevel.append(node.right)
            # Increment depth as we move to the next level of nodes
            depth += 1
            # Update current to the next level
            current = nxtlevel
        
        