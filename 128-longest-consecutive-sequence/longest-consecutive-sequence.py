class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted list.

        :param nums: List of integers
        :return: Length of the longest consecutive sequence
        """
        # If the input list is empty, return 0 since there are no sequences
        if not nums:
            return 0

        # Get the size of the input list
        n = len(nums)

        # Initialize a list to store the length of the longest sequence at each index
        sequence = [1] * n

        # A new list to store sorted unique elements using binary search for insertion
        sortedarray = []

        # Insert elements into sortedarray in sorted order using binary search
        for idx, num in enumerate(nums):
            index = bisect.bisect_left(sortedarray, num)  # Find position for insertion
            sortedarray.insert(index, num)  # Insert element at the correct position

        # Iterate over the sorted array to find the longest consecutive sequence
        for idx in range(1, n):
            # If current number is exactly 1 more than the previous, it's a part of the sequence
            if sortedarray[idx] - sortedarray[idx - 1] == 1:
                sequence[idx] = sequence[idx - 1] + 1
            # If current number is the same as the previous one, inherit the previous sequence length
            elif sortedarray[idx] - sortedarray[idx - 1] == 0:
                sequence[idx] = sequence[idx - 1]

        # Return the maximum length found in the sequence array
        return max(sequence)
        
        
