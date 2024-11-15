# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # If the tree is empty, return a list containing an empty string
        if not root:
            return [""]
        
        # Stack to perform iterative traversal
        # Each element in the stack is a pair [current_node, path_so_far]
        stack = [[root, str(root.val)]]
        
        # List to store all root-to-leaf paths
        result = []

        # Perform a depth-first traversal using a stack
        while stack:
            # Pop the current node and its path from the stack
            current, string = stack.pop()

            # If the current node is a leaf, add its path to the result
            if not current.left and not current.right:
                result.append(string)
            
            # If the current node has a right child, append it to the stack
            # Add the value of the right child to the path
            if current.right:
                stack.append([current.right, string + "->" + str(current.right.val)])
            
            # If the current node has a left child, append it to the stack
            # Add the value of the left child to the path
            if current.left:
                stack.append([current.left, string + "->" + str(current.left.val)])
        
        # Return the list of all root-to-leaf paths
        return result



        