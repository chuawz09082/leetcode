class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Create a dictionary to count the frequency of each character
        char_dict = collections.defaultdict(int)  # Initialize a defaultdict for counting

        # Step 2: Iterate through the string and update the frequency of each character
        for c in s:
            char_dict[c] += 1  # Increment the count for the character `c`

        # Step 3: Sort the dictionary items by frequency in descending order
        # Use `-x[1]` to sort by frequency in descending order
        char_dict = dict(sorted(char_dict.items(), key=lambda x: -x[1]))

        # Step 4: Initialize an empty string to store the result
        result = ""

        # Step 5: Iterate through the sorted dictionary and construct the result string
        for key, value in char_dict.items():
            # Append the character `key` repeated `value` times to the result string
            result += key * value

        # Step 6: Return the final sorted string
        return result
        