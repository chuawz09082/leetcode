# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects the node where a cycle begins in a linked list. 
        If there is no cycle, returns None.

        Args:
        head (Optional[ListNode]): The head of the linked list.

        Returns:
        Optional[ListNode]: The node where the cycle begins, or None if no cycle exists.
        """
        # Initialize a set to store visited nodes
        seen = set()

        # Start traversing the linked list from the head
        current = head

        # Traverse until the end of the list
        while current:
            # If the current node is already in the set, a cycle is detected
            if current in seen:
                return current  # Return the node where the cycle starts

            # Add the current node to the set of seen nodes
            seen.add(current)

            # Move to the next node in the linked list
            current = current.next

        # If the end of the list is reached without detecting a cycle, return None
        return None


        