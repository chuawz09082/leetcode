# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the tree is empty, return None
        if not root:
            return 
        # If the tree consists of a single node, return that node as the lowest common ancestor (LCA)
        if not root.left and not root.right:
            return root
        
        # Dictionary to keep track of parent-child relationships
        parentdict = {}
        # List to store the current level nodes during traversal
        current = [root]

        # Perform level-order traversal to find the deepest leaves
        while current:
            nxtlevel = []  # List to store the next level of nodes
            leaves = []    # List to store all leaf nodes at the current level

            for node in current:
                # If the node is a leaf, add it to the leaves list
                if not node.left and not node.right:
                    leaves.append(node)
                    continue
                # If the node has a left child, record the parent and add the child to the next level
                if node.left:
                    parentdict[node.left] = node
                    nxtlevel.append(node.left)
                # If the node has a right child, record the parent and add the child to the next level
                if node.right:
                    parentdict[node.right] = node
                    nxtlevel.append(node.right)
            
            # Move to the next level
            current = nxtlevel
        
        # List to store the common ancestors during the backtracking process
        commontree = []
        
        # Backtrack from the deepest leaves to find the LCA
        while len(leaves) != 1:  # Continue until there's only one node left (the LCA)
            for leaf in leaves:
                # Get the parent of the current leaf
                parent = parentdict[leaf]
                # If the parent is not already in the common tree list, add it
                if not commontree or parent not in commontree:
                    commontree.append(parent)
            # Update leaves to the current list of common ancestors
            leaves = commontree
            # Reset the common tree list for the next iteration
            commontree = []
        
        # The remaining single node in leaves is the LCA
        return leaves[0]


