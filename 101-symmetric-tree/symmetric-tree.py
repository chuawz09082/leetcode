# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Helper function to check if two subtrees are mirrors of each other
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # If both subtrees are empty, they are mirrors
        if not left and not right:
            return True
        # If only one of the subtrees is empty, they are not mirrors
        if not left or not right:
            return False
        # Check if the current nodes are equal and recursively check their children
        # - left's left child with right's right child
        # - left's right child with right's left child
        return (left.val == right.val and 
                self.isMirror(left.left, right.right) and 
                self.isMirror(left.right, right.left))

    # Main function to check if a tree is symmetric
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # If the tree is empty, it is symmetric
        if not root:
            return True
        # Otherwise, check if the left and right subtrees are mirrors of each other
        else:
            return self.isMirror(root.left, root.right)
        
        
        

        