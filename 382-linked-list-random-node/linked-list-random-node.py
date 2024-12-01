# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        """
        Initializes the Solution object with the given linked list.

        Args:
        head (Optional[ListNode]): The head of the linked list.
        """
        self.head = head  # Store the head of the linked list
        self.size = 0  # Variable to store the size of the linked list
        self.lstnum = []  # List to store all values from the linked list

        # Traverse the linked list to populate lstnum and compute its size
        current = head
        while current:
            self.lstnum.append(current.val)  # Append the current node's value to lstnum
            self.size += 1  # Increment the size counter
            current = current.next  # Move to the next node

    def getRandom(self) -> int:
        """
        Returns a random node's value from the linked list.

        Returns:
        int: The value of a randomly selected node.
        """
        # Generate a random index between 0 and size-1
        random_number = random.randint(0, self.size - 1)

        # Return the value at the randomly selected index
        return self.lstnum[random_number]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()