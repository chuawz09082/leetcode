class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Finds the maximum number of consecutive 1s in the binary list `nums`
        if at most one 0 is flipped to 1.

        Args:
        nums (List[int]): A list of binary integers (0s and 1s).

        Returns:
        int: The maximum length of consecutive 1s after flipping at most one 0.
        """
        # If the list contains 0 or 1 zeros, the entire list can become consecutive 1s
        if nums.count(0) <= 1:
            return len(nums)
        
        # Find all the indexes of zeros in the list
        indexes_of_zero = [index for index, num in enumerate(nums) if num == 0]

        # Calculate the maximum consecutive 1s by flipping the first or last 0
        maxlength = max(indexes_of_zero[1], len(nums) - 1 - indexes_of_zero[-2])

        # If there are exactly 2 zeros, return the computed maximum length
        if nums.count(0) == 2:
            return maxlength

        # Iterate through the list of zero indexes and calculate possible lengths
        while indexes_of_zero:
            # Get the index of the current zero to consider flipping
            start = indexes_of_zero.pop(0)
            
            # If only one zero is left in the list, calculate the maximum length
            if len(indexes_of_zero) == 1:
                return max(maxlength, len(nums) - 1 - start)

            # Update the maximum length considering the distance between consecutive zeros
            maxlength = max(maxlength, indexes_of_zero[1] - start - 1)


        