class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Removes the minimum number of parentheses to make the input string valid.
        Ensures every '(' has a matching ')' and vice versa.

        :param s: Input string containing letters and parentheses.
        :return: Valid string after removing extra parentheses.
        """

        # Stack to keep track of unmatched '(' positions
        stack = []
        
        # List to store indices of unmatched parentheses that should be removed
        ends = []

        # Result string to store the final output
        result = ""

        # First pass: Identify unmatched parentheses
        for idx, char in enumerate(s):
            
            # If the character is not a parenthesis, ignore it
            if char != '(' and char != ')':
                continue

            # If it's a closing parenthesis ')' and there is an unmatched opening '(', pop it
            if char == ')' and stack and stack[-1] == '(':
                stack.pop()
                ends.pop()  # Remove the matching '(' index from ends as it's now valid
                continue

            # Otherwise, push the unmatched parenthesis onto the stack
            stack.append(char)
            ends.append(idx)  # Store the index of the unmatched parenthesis

        # If there are no unmatched parentheses, return the original string
        if not ends:
            return s

        # If every character is an unmatched parenthesis, return an empty string
        if len(ends) == len(s):
            return ""

        # Second pass: Construct the valid string by skipping indices in `ends`
        start = 0
        for num in ends:
            result += s[start:num]  # Append characters before the invalid parenthesis
            start = num + 1  # Skip the invalid parenthesis
        
        result += s[start:]  # Append remaining valid characters after the last removed index

        return result
        