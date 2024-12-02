# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a list to store node values
        listnum = []
        # Pointer to traverse the linked list
        current = head

        while current:  # Traverse through the linked list
            value = current.val  # Get the value of the current node
            
            # If the current value is 0, skip this node and move to the next
            if value == 0:
                current = current.next
                continue

            # Create a reversed list to check for zero-sum sublists
            reverse = list(reversed(listnum))
            pointer = 1  # Initialize pointer to traverse through the reversed list
            
            # Check if any sublist ending at the current node sums to zero
            while pointer <= len(listnum): 
                if value + sum(reverse[0:pointer]) == 0:  # Check if the sum is zero
                    break  # Exit the loop if a zero-sum sublist is found
                pointer += 1
            
            # If a zero-sum sublist is found
            if value + sum(reverse[0:pointer]) == 0:
                # Remove the elements of the zero-sum sublist from `listnum`
                while listnum and pointer > 0:
                    listnum.pop()
                    pointer -= 1
            else:
                # If no zero-sum sublist is found, add the current value to `listnum`
                listnum.append(current.val)
            
            # Move to the next node in the linked list
            current = current.next

        # If `listnum` is empty, return None (no nodes left after removing zero-sum sublists)
        if not listnum:
            return None

        # Create a new linked list using the values in `listnum`
        newNode = ListNode(listnum.pop(0))  # Initialize the new linked list with the first value
        currentnew = newNode  # Pointer to build the new linked list

        while listnum:  # Iterate through the remaining values in `listnum`
            # Add each value as a new node in the linked list
            currentnew.next = ListNode(listnum.pop(0))
            currentnew = currentnew.next

        # Return the head of the new linked list
        return newNode
        