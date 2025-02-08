class Solution:
    def makePalindrome(self, s: str) -> bool:
        """
        Determines if a given string can be converted into a palindrome by changing at most two characters.

        :param s: The input string.
        :return: True if the string can be made into a palindrome with at most two changes, otherwise False.
        """

        # Initialize two pointers for comparing characters from both ends
        left = 0
        right = len(s) - 1

        # Counter to track the number of character mismatches
        count = 0

        # Iterate while the left pointer is less than or equal to the right pointer
        while left <= right:
            
            # If characters at both ends are different, increment the mismatch counter
            if s[left] != s[right]:
                count += 1

                # If more than two characters need to be changed, return False
                if count > 2:
                    return False
            
            # Move pointers towards the center
            left += 1
            right -= 1
        
        # If the loop completes without exceeding two mismatches, return True
        return True
        