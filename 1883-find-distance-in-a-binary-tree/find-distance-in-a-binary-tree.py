# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        """
        Finds the distance between two nodes with values `p` and `q` in a binary tree.

        @param root: Optional[TreeNode] - The root of the binary tree.
        @param p: int - The value of the first node.
        @param q: int - The value of the second node.
        @return: int - The distance between the two nodes.
        """
        # If the two nodes are the same, the distance is 0.
        if p == q:
            return 0

        # Initialize the current level with the root node and its value path.
        current = [[root, [root.val]]]
        leftlist = None  # Stores the path to the node with value `p`.
        rightlist = None  # Stores the path to the node with value `q`.

        # Perform a level-order traversal (BFS) to find paths to `p` and `q`.
        while current:
            nxtlevel = []  # List to store nodes for the next level.

            # Iterate over all nodes in the current level.
            for node, vallist in current:
                # If the current node value matches `p`, store its path.
                if node.val == p:
                    leftlist = vallist
                    # If the path to `q` is already found, stop further processing.
                    if rightlist:
                        current = []
                        break

                # If the current node value matches `q`, store its path.
                if node.val == q:
                    rightlist = vallist
                    # If the path to `p` is already found, stop further processing.
                    if leftlist:
                        current = []
                        break

                # Add the left child to the next level with the updated path.
                if node.left:
                    nxtlevel.append([node.left, vallist + [node.left.val]])
                # Add the right child to the next level with the updated path.
                if node.right:
                    nxtlevel.append([node.right, vallist + [node.right.val]])
              
            # Move to the next level.
            current = nxtlevel

        # Remove the common prefix of both paths (from the root to the lowest common ancestor).
        while leftlist and rightlist and leftlist[0] == rightlist[0]:
            leftlist.pop(0)
            rightlist.pop(0)
        
        # The remaining lengths of both paths represent the distance between `p` and `q`.
        return len(leftlist) + len(rightlist)
       
        

            



        