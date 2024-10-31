# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        # Array to store the sum of node values at each level
        array_sum = []

        # Helper function for recursive depth-first traversal
        def helper(root, depth):
            # Base case: if the node is None, return
            if not root:
                return
            
            # If this is the first node at the current depth, initialize the sum for this level
            if depth == len(array_sum):
                array_sum.append(root.val)
            else:
                # Otherwise, add the node's value to the existing sum for this level
                array_sum[depth] += root.val
            
            # Recur for the left and right children, increasing depth by 1
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        # Start the recursive traversal from the root at depth 0
        helper(root, 0)
        
        # Find the level with the minimum sum in `array_sum` and return its (1-based) index
        return array_sum.index(min(array_sum)) + 1


        