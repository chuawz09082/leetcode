class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Convert the number to a list of characters (digits) for easier manipulation
        lst = list(str(n))
        
        # Loop until we have the final answer
        while lst:
            # If there's only one digit, it's already monotone, so we return it directly
            if len(lst) == 1:
                return int("".join(lst))

            # Loop from the end of the list to the beginning
            for i in range(len(lst) - 1, 0, -1):
                print(lst)  # Debug statement to track the list's state at each iteration
                
                # Check if the current digit is less than the previous one
                if int(lst[i]) < int(lst[i - 1]):
                    pos = i  # Record the position where the monotone condition fails
                    break  # Exit the loop as we've found where to adjust the number
                
                # If we've reached the second position without finding a decreasing pair
                # then the number is already monotone increasing, so we return it
                if i == 1:
                    return int("".join(lst))

            # Replace all digits from the found position onward with zeros to make the number monotone
            zeros = ['0' for _ in range(len(lst) - pos)]
            lst = lst[:pos] + zeros

            # Subtract 1 from the current number and convert it back to a list of digits
            # This ensures that the monotone property is preserved
            lst = list(str(int("".join(lst)) - 1))

        # Convert the final list of digits back to an integer and return it
        return int("".join(lst))

