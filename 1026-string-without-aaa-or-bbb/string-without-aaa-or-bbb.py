class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        # Base case: If the sum of 'a' and 'b' is 3 or less, construct the string directly
        if a + b <= 3:
            s = ""
            s += "a" * a
            s += "b" * b
            return s

        s = ""  # Result string to be built and returned

        # Determine which character is more frequent and assign accordingly
        if b > a:
            chars = "b"  # Character with higher count
            charn = "a"  # Character with lower count
        else:
            chars = "a"
            charn = "b"

        # Assign counts for the more frequent and less frequent characters
        totals = max(a, b)  # Total count of the more frequent character
        totaln = min(a, b)  # Total count of the less frequent character
        remains = totals    # Remaining count of the more frequent character
        remainn = totaln    # Remaining count of the less frequent character

        # Build the string while ensuring no 3 consecutive characters are the same
        while remains > remainn and remainn > 0 and remains > 0:
            # Add up to 2 characters of the more frequent type
            mins = min(2, remains)
            s += chars * mins
            remains -= mins

            # Add 1 character of the less frequent type
            minn = min(1, remainn)
            s += charn * minn
            remainn -= minn

        # Handle any remaining characters if one type is exhausted
        if remains > 0 or remainn > 0:
            if remainn == 0:
                # If no more of the less frequent character, add remaining more frequent characters
                s += chars * remains
                return s
            
            # For remaining positions, alternate between characters
            for i in range(a + b - len(s)):
                if len(s) > 0 and s[-1] == "b":
                    s += "a"
                else:
                    s += "b"

        # Return the final constructed string
        return s



