# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the minimum number of moves required to distribute coins in a binary tree such that
        each node has exactly one coin. Each move involves transferring one coin between parent and child nodes.

        @param root: The root of the binary tree.
        @return: The minimum number of moves required.
        """

        self.moves = 0  # Initialize a variable to store the total number of moves.

        def postorder(node: Optional[TreeNode]) -> int:
            """
            Performs a postorder traversal of the binary tree to calculate the coin balance at each node.
            
            @param node: The current node being processed.
            @return: The net balance of coins for the current subtree. Positive balance means surplus coins,
                     while negative balance means a deficit.
            """
            if not node:
                # Base case: If the node is None, it contributes nothing to the balance.
                return 0
            
            # Recursively calculate the balance for the left and right subtrees.
            left = postorder(node.left)
            right = postorder(node.right)

            # Calculate the current node's balance:
            #   - Add its value (node.val) to the balance from its children (left + right).
            #   - Subtract 1 because the node itself needs one coin.
            balance = node.val + left + right - 1

            # Update the total moves:
            #   - Add the absolute value of the balance, which represents the coins moved to or from this node.
            self.moves += abs(balance)

            # Return the balance to the parent node.
            return balance

        # Start the postorder traversal from the root node.
        postorder(root)

        # Return the total number of moves calculated.
        return self.moves     


        