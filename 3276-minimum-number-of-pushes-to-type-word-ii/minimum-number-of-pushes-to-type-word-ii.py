class Solution:
    def minimumPushes(self, word: str) -> int:
        """
        Calculates the minimum number of pushes required to type a given word 
        on a keypad with a limited number of keys per screen (8 keys per screen).

        @param word: str - The input word.
        @return: int - The minimum number of pushes required.
        """
        # Count the frequency of each letter in the word using Counter from collections module.
        count = Counter(list(word))
        
        # If the number of unique letters is less than 9, all letters can fit on one keypad screen.
        # In this case, the total number of pushes equals the length of the word.
        if len(count.keys()) < 9:
            return len(word)
        
        # Sort the letters by their frequency in descending order.
        # `keysvalues` is a list of tuples (letter, frequency) sorted by frequency.
        keysvalues = sorted(count.items(), key=lambda x: -x[1])
        
        total = 0  # Total pushes required.
        push = 0   # Current number of pushes for the current keypad screen.

        # Iterate through the sorted letters and their frequencies.
        for i in range(len(keysvalues)):
            # Unpack the letter and its frequency.
            letter, count = keysvalues[i][0], keysvalues[i][1]

            # Every 8th key requires switching to a new keypad screen.
            if i % 8 == 0:
                push += 1  # Increment the push count for the new screen.

            # Add the pushes required for the current letter's frequency to the total.
            total += push * count
        
        # Return the total number of pushes.
        return total




        