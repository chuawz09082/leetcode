class MyLinkedList:

    def __init__(self):
        # Initialize the linked list with no value and no next node
        self.val = None
        self.next = None

    def get(self, index: int) -> int:
        """
        Get the value of the node at the given index.
        If the index is invalid, return -1.
        """
        current = self  # Start traversal from the head of the list
        start = 0

        # Traverse the list until reaching the desired index
        while current and start < index:
            current = current.next
            start += 1

        # If the index is out of bounds or the current node has no value, return -1
        if not current or current.val == None:
            return -1

        # Return the value of the node at the given index
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a new node with the given value at the head of the linked list.
        """
        # If the list is empty, set the head value
        if self.val == None:
            self.val = val
            return

        # Create a new node to store the current head value and next pointer
        newnext = MyLinkedList()
        newnext.val = self.val
        newnext.next = self.next

        # Update the head to the new value
        self.val = val
        self.next = newnext

    def addAtTail(self, val: int) -> None:
        """
        Add a new node with the given value at the tail of the linked list.
        """
        # If the list is empty, set the head value
        if self.val == None:
            self.val = val
            return

        # Create a new node for the tail
        newnext = MyLinkedList()
        newnext.val = val

        # Traverse the list to find the last node
        current = self
        while current.next:
            current = current.next
        
        # Append the new node to the last node
        current.next = newnext

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a new node with the given value before the index-th node in the linked list.
        If index is equal to the length of the list, the node will be appended to the end.
        If index is greater than the length, the node will not be inserted.
        """
        # If the index is 0, add the node at the head
        if index == 0:
            self.addAtHead(val)
            return

        # Create the new node
        newNode = MyLinkedList()
        newNode.val = val

        # Traverse the list to find the (index-1)-th node
        current = self
        start = 0
        while current and start < index-1:
            current = current.next
            start += 1

        # If index is out of bounds, do nothing
        if not current:
            return

        # Insert the new node at the specified index
        newNode.next = current.next
        current.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the node at the given index in the linked list.
        If the index is invalid, do nothing.
        """
        # If the index is 0, update the head
        if index == 0:
            if self.next:  # If there is a next node, update head value and pointer
                self.val = self.next.val
                self.next = self.next.next
            else:  # If this is the only node, reset the list
                self.val = None
                self.next = None
            return

        # Traverse the list to find the (index-1)-th node
        current = self
        start = 0
        while current and current.next and start < index-1:
            current = current.next
            start += 1

        # If the index is out of bounds, do nothing
        if not current or not current.next:
            return

        # Remove the node at the specified index
        current.next = current.next.next

    def display(self):
        """
        Display the linked list for debugging and visualization.
        """
        current = self
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)