# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Convert list to set for O(1) lookup
        target_nodes = set(node.val for node in nodes)
        
        def dfs(node):
            if not node:
                return None
            
            # If the current node is in the target list, return it
            if node.val in target_nodes:
                return node
            
            # Search for nodes in left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right are not None, current node is the LCA
            if left and right:
                return node
            
            # Otherwise, return the non-null result (either left or right)
            return left if left else right
        
        return dfs(root)


        
            
            
        