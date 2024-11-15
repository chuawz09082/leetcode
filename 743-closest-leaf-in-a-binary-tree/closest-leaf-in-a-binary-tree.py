# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # Dictionary to store parent relationships of each node
        parentdict = {}

        # Initialize a stack for BFS traversal to populate the parent dictionary
        stack = [root]

        while stack:
            nxtlevel = []  # List to store nodes at the next level
            for node in stack:
                # If the current node's value matches the target value `k`, mark it as the start node
                if node.val == k:
                    startnode = node
                # Add the left child to the parent dictionary and the next level, if it exists
                if node.left:
                    parentdict[node.left] = node
                    nxtlevel.append(node.left)
                # Add the right child to the parent dictionary and the next level, if it exists
                if node.right:
                    parentdict[node.right] = node
                    nxtlevel.append(node.right)
            # Move to the next level in BFS traversal
            stack = nxtlevel
        
        # Start the BFS from the node with value `k`
        startlvl = [startnode]
        seen = set()  # Set to track visited nodes

        while startlvl:
            nxtdepth = []  # List to store nodes at the next depth level
            for node in startlvl:
                # If the current node is a leaf, return its value
                if not node.left and not node.right:
                    return node.val
                # Mark the current node as visited
                seen.add(node.val)
                # If the parent of the current node exists and hasn't been visited, add it to the next level
                if node in parentdict and parentdict[node].val not in seen:
                    nxtdepth.append(parentdict[node])
                # If the left child exists and hasn't been visited, add it to the next level
                if node.left and node.left.val not in seen:
                    nxtdepth.append(node.left)
                # If the right child exists and hasn't been visited, add it to the next level
                if node.right and node.right.val not in seen:
                    nxtdepth.append(node.right)
            # Move to the next level in BFS traversal
            startlvl = nxtdepth

        


            


        

        