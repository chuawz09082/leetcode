# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        Determines whether two binary trees are flip equivalent.

        Flip equivalence means two trees are identical or can become identical 
        by flipping left and right children at any number of nodes.

        @param root1: The root of the first binary tree.
        @param root2: The root of the second binary tree.
        @return: True if the trees are flip equivalent, False otherwise.
        """

        def bfs(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            """
            Recursively checks if two subtrees are flip equivalent.

            @param node1: The root of the first subtree.
            @param node2: The root of the second subtree.
            @return: True if the subtrees are flip equivalent, False otherwise.
            """
            # Base case: Both nodes are None, they are trivially equivalent.
            if not node1 and not node2:
                return True
            # If one of the nodes is None but not the other, they are not equivalent.
            if not node1 or not node2:
                return False
            # Check if the current nodes have the same value and their children are equivalent:
            # 1. Without flipping (left-left, right-right).
            # 2. With flipping (left-right, right-left).
            return (node1.val == node2.val and 
                    ((bfs(node1.left, node2.left) and bfs(node1.right, node2.right)) or 
                     (bfs(node1.left, node2.right) and bfs(node1.right, node2.left))))
        
        # Start the recursive comparison from the root of both trees.
        return bfs(root1, root2)

        