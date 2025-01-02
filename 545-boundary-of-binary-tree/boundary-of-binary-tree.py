# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the boundary of a binary tree as a list of node values.

        The boundary includes:
        1. Root node (if not a leaf).
        2. Left boundary (excluding the leftmost leaf).
        3. All leaf nodes in left-to-right order.
        4. Right boundary (excluding the rightmost leaf), in reverse order.

        @param root: The root of the binary tree.
        @return: A list of integers representing the boundary of the tree.
        """
        if not root:
            return []

        # Special case: if the root is the only node, return its value.
        if not root.left and not root.right:
            return [root.val]

        # Initialize boundary with the root value.
        boundary = [root.val]

        def is_leaf(node: Optional[TreeNode]) -> bool:
            """
            Determines if a node is a leaf (has no children).
            
            @param node: The node to check.
            @return: True if the node is a leaf, False otherwise.
            """
            return not node.left and not node.right

        def add_leaves(node: Optional[TreeNode]):
            """
            Adds all leaf nodes in the tree to the boundary in left-to-right order.
            
            @param node: The current node being processed.
            """
            if node.left:
                add_leaves(node.left)  # Traverse the left subtree.
            if node.right:
                add_leaves(node.right)  # Traverse the right subtree.
            if is_leaf(node):  # If the current node is a leaf, add it to the boundary.
                boundary.append(node.val)

        def add_left_bdy(node: Optional[TreeNode]) -> List[int]:
            """
            Collects the left boundary of the tree, excluding the leftmost leaf.
            
            @param node: The current node being processed.
            @return: A list of values forming the left boundary.
            """
            tmp = []
            while node:
                if not is_leaf(node):  # Exclude leaves from the left boundary.
                    tmp.append(node.val)
                node = node.left if node.left else node.right  # Move left or fallback to right.
            return tmp

        def add_right_bdy(node: Optional[TreeNode]) -> List[int]:
            """
            Collects the right boundary of the tree, excluding the rightmost leaf, in reverse order.
            
            @param node: The current node being processed.
            @return: A list of values forming the right boundary in reverse order.
            """
            tmp = []
            while node:
                if not is_leaf(node):  # Exclude leaves from the right boundary.
                    tmp.append(node.val)
                node = node.right if node.right else node.left  # Move right or fallback to left.
            return tmp[::-1]  # Reverse the collected right boundary values.

        # Add left boundary values (excluding leaves).
        boundary += add_left_bdy(root.left)

        # Add all leaf nodes in left-to-right order.
        add_leaves(root)

        # Add right boundary values (excluding leaves and in reverse order).
        boundary += add_right_bdy(root.right)

        return boundary

                




        

