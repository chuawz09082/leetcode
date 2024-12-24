# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Removes nodes from a linked list such that each node's value is not smaller 
        than all the nodes following it. The remaining nodes are returned as a new linked list.
        
        @param head: The head of the input linked list.
        @return: The head of the modified linked list with nodes removed as per the condition.
        """
        # Step 1: Extract values from the linked list into a list while maintaining the required order
        lstnum = []  # Stack to store the filtered values
        current = head  # Pointer to traverse the linked list
        
        # Traverse the linked list
        while current:
            # Remove elements from the stack if they are smaller than the current value
            # This ensures that only valid elements are retained in lstnum
            while lstnum and lstnum[-1] < current.val:
                lstnum.pop()
            
            # Add the current value to the stack
            lstnum.append(current.val)
            
            # Move to the next node in the linked list
            current = current.next
        
        # Step 2: Reconstruct the linked list using the filtered values in lstnum
        # Initialize the head of the new linked list using the first value in lstnum
        result = ListNode(lstnum.pop(0))
        current = result  # Pointer to traverse the newly created linked list
        
        # Add the remaining values from lstnum to the new linked list
        while lstnum:
            # Create a new node with the next value and attach it to the current node
            current.next = ListNode(lstnum.pop(0))
            
            # Move to the next node in the newly created linked list
            current = current.next
        
        # Return the head of the reconstructed linked list
        return result