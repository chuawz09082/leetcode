class PhoneDirectory:
    def __init__(self, maxNumbers: int):
        """
        Initialize the phone directory with the maximum numbers it can hold.
        
        Args:
        maxNumbers (int): The maximum number of phone numbers in the directory.

        Attributes:
        lst (List[Optional[int]]): A list to track available and assigned numbers. 
                                   Initially filled with `None`, indicating all numbers are available.
        """
        self.lst = [None for _ in range(maxNumbers)]

    def get(self) -> int:
        """
        Provide an available number. If no number is available, return -1.
        
        Returns:
        int: The first available number, or -1 if no numbers are available.
        """
        # Check if there are any `None` entries in the list (indicating availability)
        if self.lst.count(None) == 0:
            return -1
        
        # Find the first available index (None) and mark it as assigned
        first_index = self.lst.index(None)
        self.lst[first_index] = first_index
        return first_index

    def check(self, number: int) -> bool:
        """
        Check if a specific number is available.
        
        Args:
        number (int): The number to check availability for.
        
        Returns:
        bool: True if the number is available (None), False otherwise.
        """
        return self.lst[number] == None

    def release(self, number: int) -> None:
        """
        Release a previously assigned number, making it available again.
        
        Args:
        number (int): The number to release.
        """
        self.lst[number] = None
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)