class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Find the k most frequent words from a list of words, sorted by frequency and lexicographical order.
        
        Args:
        words (List[str]): A list of words.
        k (int): The number of most frequent words to return.
        
        Returns:
        List[str]: A list of the k most frequent words, sorted by frequency and lexicographical order.
        """
        # Step 1: Create a dictionary to count the frequency of each word
        count_dict = collections.defaultdict(int)

        # Step 2: Iterate through the list of words and update the frequency of each word
        for word in words:
            count_dict[word] += 1  # Increment the count for the word

        # Step 3: Sort the dictionary items by frequency (descending) and by lexicographical order (ascending) for ties
        # Convert the sorted items back into a dictionary
        count_dict = dict(sorted(count_dict.items(), key=lambda x: (-x[1], x[0])))

        # Step 4: Extract the sorted keys (words) from the dictionary
        keys = list(count_dict.keys())

        # Step 5: Return the first k words from the sorted keys
        return keys[:k]
        