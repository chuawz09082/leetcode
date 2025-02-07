class Solution:
    def partitionString(self, s: str) -> int:
        # Initialize a list to store substrings that do not contain duplicate characters
        result = []
        
        # Start with the first character as the initial substring
        current = s[0]

        # Iterate through the string from the second character onwards
        for i in range(1, len(s)):
            # If the current character is already in the substring, start a new substring
            if s[i] in current:
                result.append(current)  # Store the completed substring
                current = s[i]  # Start a new substring with the current character
            else:
                current += s[i]  # Append the character to the current substring
                
        # Append the last accumulated substring to the result list
        result.append(current)

        # Return the number of partitions created
        return len(result)
        