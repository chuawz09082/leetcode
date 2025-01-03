# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a bottom-up level order traversal of a binary tree.

        @param root: The root of the binary tree.
        @return: A list of lists containing node values, level by level from bottom to top.
        """
        # If the root is None, return an empty list.
        if not root:
            return []
        
        result = []  # List to store the levels of the tree.
        current = [root]  # Initialize the current level with the root node.

        # Perform level order traversal.
        while current:
            nxtlevel = []  # List to store nodes for the next level.
            currentlevel = []  # List to store values of nodes at the current level.

            # Process all nodes in the current level.
            for node in current:
                currentlevel.append(node.val)  # Add the current node's value to the level.
                # Add the left child to the next level if it exists.
                if node.left:
                    nxtlevel.append(node.left)
                # Add the right child to the next level if it exists.
                if node.right:
                    nxtlevel.append(node.right)
            
            result.append(currentlevel)  # Append the current level values to the result.
            current = nxtlevel  # Move to the next level.

        # Reverse the result to achieve bottom-up order and return it.
        return result[::-1]          




        