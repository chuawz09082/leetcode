# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Step 1: Calculate the total length of the linked list
        length = 0  # Initialize length counter
        current = head  # Start traversing from the head
        while current:  # Traverse until the end of the linked list
            length += 1  # Increment length for each node
            current = current.next  # Move to the next node
        
        # Step 2: Determine the base group size and the remainder
        grouplength = length // k  # Calculate the minimum number of nodes in each group
        remainder = length % k  # Calculate the number of groups that need an extra node
        
        # Step 3: Initialize portions array to store the size of each group
        portions = [grouplength for _ in range(k)]  # Start with the base group size for all groups
        start = 0  # Pointer to distribute the remainder

        # Distribute the remainder among the first groups
        while remainder:
            portions[start] += 1  # Add an extra node to the current group
            start += 1  # Move to the next group
            remainder -= 1  # Decrease the remainder

        # Step 4: Split the linked list based on the calculated portions
        result = []  # List to store the resulting parts
        current = head  # Reset current to the head of the list

        while portions:  # Process each group size in portions
            length = portions.pop(0)  # Get the size of the current group
            if length == 0:  # If the group size is 0, append None
                result.append(None)
                continue
            
            # Create a new linked list for the current group
            newNode = ListNode(current.val)  # Initialize the new list with the current node's value
            currentnew = newNode  # Pointer for building the new linked list
            
            while length > 1:  # Add the remaining nodes for the current group
                currentnew.next = ListNode(current.next.val)  # Create a new node with the next value
                length -= 1  # Decrease the remaining length
                current = current.next  # Move to the next node in the original list
                currentnew = currentnew.next  # Move to the next node in the new list
            
            result.append(newNode)  # Append the completed group to the result
            current = current.next  # Move to the next node for the next group
            
        # Step 5: Return the list of split parts
        return result

        