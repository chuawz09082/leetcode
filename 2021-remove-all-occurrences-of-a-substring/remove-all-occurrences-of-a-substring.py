class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Initialize the starting index for searching substrings
        start = 0
        # Store the length of the substring to be removed
        n = len(part)

        # Iterate through the string while there's enough room to find the substring
        while start < len(s) - len(part) + 1:
            # Check if the current window matches the substring to be removed
            if s[start:start + n] == part:
                # Remove the substring by reconstructing the string without it
                s = s[:start] + s[start + n:]
                # Move back to check if the previous characters formed another occurrence
                start = max(0, start - n + 1)
            else:
                # Move forward if no match is found at the current index
                start += 1

        # Return the modified string after all occurrences are removed
        return s
