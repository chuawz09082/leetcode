# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        """
        Constructs a binary tree from a string representation.

        @param s: A string representing a binary tree in preorder traversal with parentheses.
                  Example: "4(2(3)(1))(6(5))"
        @return: The root of the constructed binary tree.
        """
        if not s:
            # Base case: If the string is empty, return None.
            return None

        # Step 1: Find the position of the first '(' which marks the start of the left subtree.
        start_left = 0
        while start_left < len(s) and s[start_left] != '(':
            start_left += 1

        # Step 2: If there are no parentheses, the string represents a single node.
        if len(s) == start_left:
            return TreeNode(int(s))

        # Step 3: Extract the root value from the string (everything before the first '(').
        root_val = int(s[:start_left])
        root = TreeNode(root_val)  # Create the root node.

        # Step 4: Locate the substring for the left child.
        left_index = start_left
        check_left = []  # Stack to track parentheses for the left subtree.

        # Traverse the string to find the closing ')' for the left subtree.
        while check_left or left_index == start_left:
            if s[left_index] == '(':
                check_left.append('(')  # Push '(' onto the stack.
            elif s[left_index] == ')':
                check_left.pop()  # Pop ')' from the stack.
            left_index += 1

        # Step 5: Recursively build the left subtree using the identified substring.
        root.left = self.str2tree(s[start_left + 1 : left_index - 1])

        # Step 6: If there are no more characters, return the constructed root.
        if left_index == len(s):
            return root


        # Step 7: Recursively build the right subtree using the identified substring.
        root.right = self.str2tree(s[left_index + 1 : len(s) - 1])

        # Step 8: Return the constructed root node.
        return root
        