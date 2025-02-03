class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []  # List to store the final justified lines
        start = 0  # Pointer to track the current word in the list

        # Process all words to form justified lines
        while start < len(words):
            current = [words[start]]  # Initialize the current line with the first word
            count = len(words[start])  # Track the total number of characters (excluding spaces)

            # Add words to the current line as long as the total length does not exceed maxWidth
            while start + 1 < len(words) and count + 1 + len(words[start + 1]) <= maxWidth:
                current[-1] += " "  # Add a space after the last word in the current line
                current.append(words[start + 1])  # Append the next word to the current line
                start += 1  # Move to the next word
                count += 1 + len(words[start])  # Update the total character count (including the space)
            
            idx = 0  # Index for distributing additional spaces

            # Distribute remaining spaces to achieve full justification
            while count < maxWidth:
                if start == len(words) - 1 and len(current) > 1:
                    # If it's the last line and there are multiple words, add spaces to the end
                    current[-1] += " "
                    count += 1
                else:
                    # For other lines, distribute spaces evenly
                    if idx % len(current) == len(current) - 1 and len(current) != 1:
                        idx += 1  # Skip adding space after the last word if there are multiple words
                        continue
                    current[idx % len(current)] += " "  # Add space to the current word
                    count += 1  # Increment the total character count
                    idx += 1  # Move to the next word for space distribution

            # Combine the words into a single justified string and add it to the result
            result.append("".join(current))
            start += 1  # Move to the next word for the next line

        return result  # Return the list of fully justified lines
