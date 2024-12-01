# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Swaps the k-th node from the beginning with the k-th node from the end in a linked list.

        Args:
        head (Optional[ListNode]): The head of the linked list.
        k (int): The position of the node to swap from both ends.

        Returns:
        Optional[ListNode]: The head of the modified linked list.
        """
        # Step 1: Traverse the linked list and store values in a list
        current = head  # Pointer to traverse the linked list
        lstnum = []  # List to store values of the nodes

        while current:  # Iterate until the end of the linked list
            lstnum.append(current.val)  # Append the current node's value to the list
            current = current.next  # Move to the next node

        # Step 2: Perform the swap between the k-th node from the start and the k-th node from the end
        swapvalue = lstnum[k-1]  # Get the value of the k-th node from the start
        lstnum[k-1] = lstnum[len(lstnum)-k]  # Replace the k-th node's value with the k-th from the end
        lstnum[len(lstnum)-k] = swapvalue  # Replace the k-th from the end with the original k-th node's value

        # Step 3: Reconstruct the linked list from the modified list of values
        newnode = ListNode(lstnum.pop(0))  # Create the new head node with the first value in the list
        current = newnode  # Pointer to construct the rest of the linked list

        while lstnum:  # While there are remaining values in the list
            current.next = ListNode(lstnum.pop(0))  # Create a new node with the next value
            current = current.next  # Move to the next node

        # Step 4: Return the head of the modified linked list
        return newnode
        
        