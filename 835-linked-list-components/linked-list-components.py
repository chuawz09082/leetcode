# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        """
        Counts the number of connected components in the linked list `head` 
        where the nodes' values belong to the list `nums`.
        
        Args:
        head (Optional[ListNode]): The head of the linked list.
        nums (List[int]): List of values to check for components.

        Returns:
        int: The number of connected components.
        """
        current = head  # Pointer to traverse the linked list
        connected = []  # List to store all connected components
        nxtlevel = []  # Temporary list to hold current connected component

        while current:  # Traverse the linked list until the end
            if current.val in nums:  # Check if current node's value is in nums
                nxtlevel.append(current.val)  # Add the value to the current component
            else:
                # If the current component exists and is completed, add it to the result
                if nxtlevel:
                    connected.append(nxtlevel)
                nxtlevel = []  # Reset for the next potential component

            current = current.next  # Move to the next node in the linked list

        # Add the last connected component if it exists
        if nxtlevel:
            connected.append(nxtlevel)
        
        # The number of connected components is the length of the `connected` list
        return len(connected)