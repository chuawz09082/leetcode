class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        Generates the longest diverse string using 'a', 'b', and 'c' such that no character
        appears more than twice consecutively.

        @param a: The number of 'a' characters available.
        @param b: The number of 'b' characters available.
        @param c: The number of 'c' characters available.
        @return: A diverse string satisfying the above condition.
        """
        # Step 1: Handle the base case where the max count of any character is <= 2.
        # In this case, no need for advanced logic. Simply concatenate the counts of each character.
        if max([a, b, c]) <= 2:
            return "a" * a + "b" * b + "c" * c

        # Step 2: Create a max-heap to store character counts and their respective letters.
        # Use negative counts to simulate a max-heap since Python's heapq is a min-heap by default.
        heap = [tuple([-a, "a"]), tuple([-b, "b"]), tuple([-c, "c"])]
        heapq.heapify(heap)  # Convert the list into a heap
        result = ""  # The final diverse string

        # Step 3: Generate the diverse string by popping elements from the heap.
        while heap and len(result) < a + b + c:  # Ensure we don't exceed the total length of characters
            count, letter = heapq.heappop(heap)  # Get the most frequent character
            if count == 0:  # If the count is 0, skip further processing
                continue

            if len(result) < 2:  # If the string has less than 2 characters, safely add two of the letter
                result += letter * 2
                count += 2  # Adjust the count since we added two
                if count < 0:  # If there are still remaining letters, push back to the heap
                    heappush(heap, (count, letter))
                continue

            # Step 4: Handle cases where the last two characters are the same as the current letter
            if result[-1] == result[-2] == letter:
                if heap:  # If there's another character available, use it
                    count2, letter2 = heappop(heap)  # Get the second most frequent character
                    if count2 == 0:  # If the second character has 0 count, skip
                        continue
                    result += letter2  # Add the second character to the result
                    count2 += 1  # Adjust the count
                    if count2 < 0:  # Push it back to the heap if more instances are available
                        heappush(heap, (count2, letter2))
                    heappush(heap, (count, letter))  # Push the original character back to the heap
                else:  # If no other characters are available, return the current result
                    return result
            else:  # If the last two characters are not the same as the current letter
                result += letter  # Add the current letter to the result
                count += 1  # Adjust the count
                if count < 0:  # Push it back to the heap if more instances are available
                    heappush(heap, (count, letter))

        # Step 5: Return the final diverse string
        return result



        
