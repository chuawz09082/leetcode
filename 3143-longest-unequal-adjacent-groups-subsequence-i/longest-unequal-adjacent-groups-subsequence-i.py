class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        """
        Removes consecutive words from the input list if they belong to the same group,
        retaining only one word per group. The resulting list contains the longest subsequence 
        of non-repeating groups.

        Args:
        words (List[str]): List of words to be processed.
        groups (List[int]): List of integers representing the group each word belongs to.

        Returns:
        List[str]: List of words representing the longest subsequence of non-repeating groups.
        """
        # Initialize a pointer to iterate through the words and groups lists
        i = 0

        # Iterate through the words list until the second-to-last word
        while i < len(words) - 1:
            # Check if the current word and the next word belong to the same group
            if groups[i] == groups[i + 1]:
                # If they belong to the same group, remove the current group and word
                groups.pop(i)
                words.pop(i)
            else:
                # Otherwise, move to the next word
                i += 1
        
        # Return the processed list of words
        return words

        