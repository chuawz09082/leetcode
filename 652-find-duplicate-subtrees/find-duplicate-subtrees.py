# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Finds all duplicate subtrees in a binary tree.

        @param root: The root of the binary tree.
        @return: A list of duplicate subtrees.
        """
        memo = collections.defaultdict(int)  # Dictionary to count occurrences of serialized subtrees
        result = []  # List to store the roots of duplicate subtrees

        def serialize(node: Optional[TreeNode]) -> str:
            """
            Serializes the subtree rooted at the given node into a string.

            @param node: The root of the subtree to serialize.
            @return: A string representation of the subtree.
            """
            if not node:
                return "#"

            # Serialize the current subtree
            subtree = f"{node.val},{serialize(node.left)},{serialize(node.right)}"

            # Count the occurrences of this serialized subtree
            memo[subtree] += 1

            # If this is the second occurrence, add the root to the result list
            if memo[subtree] == 2:
                result.append(node)

            return subtree

        # Start the serialization process
        serialize(root)

        return result
        
