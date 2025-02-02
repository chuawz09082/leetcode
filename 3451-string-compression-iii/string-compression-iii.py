class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""  # Initialize an empty string to store the compressed result

        count = 0  # Counter to keep track of consecutive characters
        start = 0  # Pointer to iterate through the string
        n = len(word)  # Length of the input string

        # Iterate through the string
        while start < n:
            current = word[start]  # Get the current character
            count += 1  # Count the current character

            # Continue counting as long as the next character is the same,
            # the count does not exceed 9, and we are within the bounds of the string
            while start + 1 < n and count + 1 <= 9 and word[start + 1] == current:
                start += 1  # Move to the next character
                count += 1  # Increment the count

            # Append the count and the character to the compressed string
            comp += str(count) + current
            
            count = 0  # Reset the count for the next group of characters
            start += 1  # Move to the next character

        return comp  # Return the final compressed string
        