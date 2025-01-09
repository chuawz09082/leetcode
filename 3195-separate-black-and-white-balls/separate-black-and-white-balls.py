class Solution:
    def minimumSteps(self, s: str) -> int:
        """
        Calculate the minimum number of steps to group all '0's together in a binary string `s`.
        
        @param s: str - A binary string consisting of '0's and '1's.
        @return: int - Minimum number of steps required to group all '0's.
        """

        # If the string contains no '0's or no '1's, no steps are needed.
        if s.count("0") == 0 or s.count("1") == 0:
            return 0

        # Get the length of the string.
        length = len(s)

        # Find the first occurrence of '0' in the string.
        start = s.index("0")

        # Initialize `lastseen`:
        # - If the first '0' is at the start of the string, set `lastseen` to 0 (first position).
        # - Otherwise, set `lastseen` to -1 since no '0' has been moved yet.
        if start != 0:
            lastseen = -1
        else:
            lastseen = 0
            start = 1  # Start processing from the second character.

        # Initialize a counter to track the total number of steps.
        steps = 0
        
        # Iterate through the string starting from `start`.
        while start < length:

            # If the current character is '0':
            if s[start] == "0":
                # Calculate the steps required to move this '0' to its position
                # adjacent to the previously moved '0'.
                steps += start - lastseen - 1

                # Update `lastseen` to the new position of the '0'.
                lastseen += 1

            # Move to the next character.
            start += 1

        # Return the total number of steps.
        return steps




        