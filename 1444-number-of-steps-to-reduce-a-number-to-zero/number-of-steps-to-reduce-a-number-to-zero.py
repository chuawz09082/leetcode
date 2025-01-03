class Solution:
    def numberOfSteps(self, num: int) -> int:
        """
        Calculates the number of steps required to reduce a given number to 0.
        A step is defined as:
        - If the number is even, divide it by 2.
        - If the number is odd, subtract 1 from it.

        @param num: The initial integer to be reduced.
        @return: The number of steps required to reduce the number to 0.
        """
        
        # Initialize a counter to track the number of steps.
        steps = 0

        # Continue the process until the number becomes 0.
        while num > 0:
            # Check if the current number is even.
            if num % 2 == 0:
                # If even, divide the number by 2.
                num = num // 2
            else:
                # If odd, subtract 1 from the number.
                num -= 1
            
            # Increment the step counter after each operation.
            steps += 1

        # Return the total number of steps taken to reduce the number to 0.
        return steps
        