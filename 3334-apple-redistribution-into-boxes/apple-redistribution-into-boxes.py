class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # Sort the capacity list in descending order to use the largest capacity boxes first
        capacity.sort(reverse=True)
        
        # Calculate the total number of apples that need to be stored
        total_apples = sum(apple)
        
        # Initialize the number of boxes used
        countbox = 0
        # Start filling boxes from the largest capacity
        start = 0

        # Loop until all apples have been placed in boxes
        while total_apples > 0:
            # Fill the current box until it reaches capacity or all apples are used
            while capacity[start] > 0:
                total_apples -= 1  # Place one apple in the box
                capacity[start] -= 1  # Decrease the remaining capacity of the current box

                # If all apples are placed, return the number of boxes used so far (index + 1)
                if total_apples == 0:
                    return start + 1

            # Move to the next box once the current one is full
            start += 1

        # If all apples are placed, return the number of boxes used
        return start
            