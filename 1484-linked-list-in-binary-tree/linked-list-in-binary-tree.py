# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """
        Determines whether there is a downward path in a binary tree that corresponds to a given linked list.
        
        Args:
        head (Optional[ListNode]): The head of the linked list.
        root (Optional[TreeNode]): The root of the binary tree.
        
        Returns:
        bool: True if a subpath exists, False otherwise.
        """
        def dfs(tree: Optional[TreeNode], idx: int) -> bool:
            """
            Depth-First Search (DFS) to check if the linked list values match a path in the tree starting from the current tree node.
            
            Args:
            tree (Optional[TreeNode]): Current tree node being evaluated.
            idx (int): Current index in the linked list values.
            
            Returns:
            bool: True if the linked list path matches, False otherwise.
            """
            # Base case: If we reach the last index of the linked list and the value matches, return True
            if idx == len(lstnum) - 1:
                return tree.val == lstnum[idx]

            # If the current tree node's value does not match the current linked list value, return False
            if tree.val != lstnum[idx]:
                return False
            
            # Recursively check the left and right children
            if tree.left and tree.right:
                return dfs(tree.left, idx + 1) or dfs(tree.right, idx + 1)
            if tree.left:
                return dfs(tree.left, idx + 1)
            if tree.right:
                return dfs(tree.right, idx + 1)
        
        # Convert the linked list into a list of values
        current = head
        lstnum = []
        while current:
            lstnum.append(current.val)
            current = current.next

        # Perform a level-order traversal (BFS) to check each tree node as a potential starting point
        currentlvl = [root]

        while currentlvl:
            # Pop the current tree node from the level
            currenttree = currentlvl.pop()
            
            # Add the right child to the level for future exploration
            if currenttree.right:
                currentlvl.append(currenttree.right)
            
            # Add the left child to the level for future exploration
            if currenttree.left:
                currentlvl.append(currenttree.left)
            
            # Check if the current tree node's value matches the head of the linked list
            # If it matches, invoke DFS to verify the entire path
            if currenttree.val == lstnum[0] and dfs(currenttree, 0):
                return True

        # If no matching path is found, return False
        return False

        