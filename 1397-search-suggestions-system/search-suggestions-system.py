class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        Finds up to 3 lexicographically smallest product suggestions for each prefix
        of the searchWord.

        @param products: List of available product names.
        @param searchWord: The word to search for product suggestions.
        @return: A list of lists where each sublist contains up to 3 product suggestions
                 for the corresponding prefix of the searchWord.
        """
        length = len(searchWord)  # Length of the search word

        def common_prefix(word1: str, word2: str) -> bool:
            """
            Checks if `word2` is a prefix of `word1`.
            
            @param word1: The longer word to check against.
            @param word2: The shorter word (prefix).
            @return: True if `word2` is a prefix of `word1`, False otherwise.
            """
            if len(word2) > len(word1):  # A prefix cannot be longer than the word itself
                return False

            # Compare character by character
            for i in range(len(word2)):
                if word1[i] != word2[i]:
                    return False
            return True

        result = []  # List to store the final result
        heap = products  # Use the input product list as the initial heap
        heapify(heap)  # Transform the product list into a min-heap
        start = 1  # Tracks the current prefix length

        # Loop through each prefix of the search word
        while start < length + 1:
            next_heap = []  # Temporary heap for the next prefix suggestions

            # Collect up to 3 products that match the current prefix
            while len(next_heap) < 3 and len(heap) > 0:
                next_word = heappop(heap)  # Pop the smallest element from the heap
                if common_prefix(next_word, searchWord[:start]):
                    heappush(next_heap, next_word)  # Add it to the next heap if it matches the prefix
            
            # Rebuild the heap with valid suggestions and remaining products
            heap = next_heap + heap
            heapify(heap)  # Re-heapify to maintain min-heap properties
            
            result.append(next_heap)  # Add the suggestions for the current prefix to the result
            start += 1  # Move to the next prefix length

        return result  # Return the final list of suggestions
            

        