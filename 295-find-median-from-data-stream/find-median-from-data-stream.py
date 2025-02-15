class MedianFinder:
    """
    A class that maintains a sorted list and efficiently finds the median 
    after each insertion.
    """

    def __init__(self):
        """
        Initializes an empty list to store numbers.
        """
        self.stack = []  # Sorted list to store numbers

    def addNum(self, num: int) -> None:
        """
        Inserts a number into the list while maintaining sorted order.

        Args:
        num (int): The number to be inserted.
        """
        # Find the correct insertion index to keep the list sorted
        idx = bisect.bisect_left(self.stack, num)
        
        # Insert the number at the found index
        self.stack.insert(idx, num)

    def findMedian(self) -> float:
        """
        Returns the median of the numbers added so far.

        Returns:
        float: The median value.
        """
        n = len(self.stack)

        # If the list has an odd number of elements, return the middle element
        if n % 2 == 1:
            return self.stack[n // 2]
        else:
            # If even, return the average of the two middle elements
            return (self.stack[n // 2] + self.stack[n // 2 - 1]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()