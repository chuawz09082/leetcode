class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        """
        Checks if there exists a pattern of length `m` in the array `arr`
        that repeats consecutively at least `k` times.

        @param arr: List[int] - The input array of integers.
        @param m: int - The length of the pattern to check for.
        @param k: int - The required number of consecutive repetitions.
        @return: bool - True if such a pattern exists, otherwise False.
        """
        
        # If `k` is 1 and the array is not empty, any single pattern satisfies the condition.
        if k == 1 and arr:
            return True

        # If the array is empty, return False as no patterns can exist.
        if not arr:
            return False

        start = 0  # Pointer to iterate over the array.

        # Iterate through the array, stopping when there are not enough elements for a full pattern of length `m`.
        while start < len(arr) - m + 1:
            # Extract the current pattern of length `m` starting at index `start`.
            curr = arr[start:start + m]
            count = 1  # Initialize the count of consecutive repetitions of the current pattern.
            startm = start + m  # Pointer to the next segment of length `m`.

            # Check subsequent segments of length `m` for the same pattern.
            while startm < len(arr) - m + 1 and arr[startm:startm + m] == curr:
                count += 1  # Increment the count for each matching segment.

                # If the pattern repeats `k` times, return True.
                if count == k:
                    return True
                
                # Move the pointer to the next segment.
                startm += m

            # Move the starting pointer to check for patterns starting at the next index.
            start += 1

        # If no valid pattern is found, return False.
        return False

        