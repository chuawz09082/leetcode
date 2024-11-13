# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # If the tree is empty, return an empty list as there are no paths to check
        if not root:
            return []
        
        # Initialize the current level with the root node and its value in a list format
        # Each element in `current` is a pair [node, path_so_far], where path_so_far is a list of node values from root to the current node
        current = [[root, [root.val]]]
        result = []  # To store paths that sum up to the target

        # Level-order traversal to find all root-to-leaf paths
        while current:
            nxtlevel = []  # Prepare to gather nodes for the next level
            for node, path in current:
                
                # Check if the current node is a leaf and if the path sum equals targetSum
                if not node.left and not node.right and sum(path) == targetSum:
                    # If it's a valid path, add it to the result list
                    result.append(path)
                
                # If the node has a left child, add it to the next level along with the updated path
                if node.left:
                    nxtlevel.append([node.left, path + [node.left.val]])
                
                # If the node has a right child, add it to the next level along with the updated path
                if node.right:
                    nxtlevel.append([node.right, path + [node.right.val]])
            
            # Move to the next level in the tree
            current = nxtlevel
        
        # Return all root-to-leaf paths that match the target sum
        return result
        
            

        