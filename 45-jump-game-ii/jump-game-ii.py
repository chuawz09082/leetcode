class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Calculates the minimum number of jumps required to reach the last index
        of the array.

        Args:
        nums (List[int]): List where each element represents the maximum number 
                          of steps you can jump forward from that position.

        Returns:
        int: The minimum number of jumps required to reach the last index.
        """
        # Initialize a list to store the minimum jumps needed to reach each index.
        # Use `float('inf')` to signify that an index is initially unreachable.
        jumps = [float('inf') for _ in range(len(nums))]

        # Base case: The first index requires 0 jumps to reach.
        jumps[0] = 0

        # Iterate through each index of the array to calculate the jumps.
        for j in range(len(nums)):
            # Get the maximum number of steps that can be taken from the current index.
            steps = nums[j]

            # Iterate through the reachable indices from the current index.
            # Limit the range to avoid going out of bounds.
            for k in range(min(steps + 1, len(nums) - j)):
                # Update the minimum jumps needed to reach the target index.
                # Compare the current value with the new possible jump count.
                jumps[j + k] = min(jumps[j + k], jumps[j] + 1)

        # The last element in the `jumps` list represents the minimum jumps 
        # needed to reach the last index.
        return jumps[-1]




        