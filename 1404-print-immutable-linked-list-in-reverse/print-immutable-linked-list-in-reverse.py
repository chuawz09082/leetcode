# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        """
        Prints the values of an immutable linked list in reverse order.

        Args:
        head (ImmutableListNode): The head of the immutable linked list.
        """

        # Step 1: Store all nodes of the linked list in a list.
        lstnode = [head]  # Initialize a list with the head node.
        currentnode = head  # Start traversal from the head node.

        while True:  # Iterate through the linked list.
            nxtnode = currentnode.getNext()  # Get the next node.
            if not nxtnode:  # If there is no next node, stop the traversal.
                break
            lstnode.append(nxtnode)  # Add the next node to the list.
            currentnode = nxtnode  # Move to the next node.

        # Step 2: Print the nodes in reverse order using the list.
        while lstnode:  # While there are nodes in the list:
            currentnode = lstnode.pop()  # Remove the last node from the list.
            currentnode.printValue()  # Print the value of the current node.


        
        