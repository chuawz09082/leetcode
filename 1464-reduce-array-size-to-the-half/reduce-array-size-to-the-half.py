
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        # Step 1: Count the frequency of each element in the array
        # This creates a dictionary where keys are the unique elements in `arr`
        # and values are the count of occurrences of those elements.
        freq_count = Counter(arr)

        # Step 2: Create a max-heap to prioritize removing the most frequent elements first.
        # Since Python's heapq is a min-heap by default, we store negative frequencies
        # to simulate a max-heap.
        max_heap = []

        # Add all frequencies as negative values into the heap
        for count in freq_count.values():
            heappush(max_heap, -count)

        # Step 3: Initialize variables to track total array size, reduced size, and removed elements
        full_length = len(arr)  # The total length of the array
        reduce_length = 0       # Tracks the length of the array after reducing
        removed_elements = 0    # Counts how many elements (sets) are removed

        # Step 4: Remove elements from the heap until the reduced length is at least half of the original
        while reduce_length < full_length // 2:
            # Pop the most frequent element (negative frequency, so we negate it)
            reduce_length += -heappop(max_heap)
            # Increment the count of removed sets
            removed_elements += 1

        # Step 5: Return the number of removed elements (minimum set size)
        return removed_elements