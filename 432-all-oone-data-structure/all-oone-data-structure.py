class AllOne:

    def __init__(self):
        """
        Initialize the data structure.
        - `self.memo` is a dictionary (using defaultdict) that stores the count of each key.
        - `self.sorted_list` is a SortedList that stores (count, key) pairs in sorted order.
        """
        self.memo = collections.defaultdict(int)  # Keeps track of the count of each key
        self.sorted_list = SortedList()  # Maintains the (count, key) pairs in sorted order
        

    def inc(self, key: str) -> None:
        """
        Increment the count of the specified key by 1.
        - If the key already exists, remove its current (count, key) pair from `sorted_list`.
        - Add the updated (count + 1, key) pair to `sorted_list`.
        - Update the count of the key in `self.memo`.
        """
        count = self.memo[key]  # Get the current count of the key

        if count > 0:
            # Remove the old (count, key) pair from the sorted list
            self.sorted_list.remove((count, key))

        # Add the new (count + 1, key) pair to the sorted list
        self.sorted_list.add((count + 1, key))
        # Update the count in the memo
        self.memo[key] += 1

        
    def dec(self, key: str) -> None:
        """
        Decrement the count of the specified key by 1.
        - Remove the current (count, key) pair from `sorted_list`.
        - If the count after decrementing is greater than 0, add the updated (count - 1, key) pair to `sorted_list`.
        - If the count becomes 0, remove the key from `self.memo`.
        """
        count = self.memo[key]  # Get the current count of the key
        # Remove the old (count, key) pair from the sorted list
        self.sorted_list.remove((count, key))
        
        if count - 1 > 0:
            # Add the new (count - 1, key) pair if the count is still greater than 0
            self.sorted_list.add((count - 1, key))
            # Update the count in the memo
            self.memo[key] -= 1
        else:
            # If the count becomes 0, remove the key from the memo
            del self.memo[key]
        

    def getMaxKey(self) -> str:
        """
        Retrieve the key with the maximum count.
        - If `sorted_list` is empty, return an empty string.
        - Otherwise, return the key associated with the last (largest count) element in `sorted_list`.
        """
        if not self.sorted_list:  # Check if the sorted list is empty
            return ""
        return self.sorted_list[-1][1]  # Return the key of the largest (count, key) pair

    def getMinKey(self) -> str:
        """
        Retrieve the key with the minimum count.
        - If `sorted_list` is empty, return an empty string.
        - Otherwise, return the key associated with the first (smallest count) element in `sorted_list`.
        """
        if not self.sorted_list:  # Check if the sorted list is empty
            return ""
        return self.sorted_list[0][1]  # Return the key of the smallest (count, key) pair
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()