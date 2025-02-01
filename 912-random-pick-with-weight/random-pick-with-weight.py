class Solution:

    def __init__(self, w: List[int]):
        # Initialize the prefix sum array to store cumulative weights
        self.prefix_sums = []
        prefix_sum = 0
        
        # Compute the prefix sums from the weights
        for weight in w:
            prefix_sum += weight  # Add the current weight to the running total
            self.prefix_sums.append(prefix_sum)  # Store the cumulative sum
        
        # Store the total sum of weights for random number generation
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        # Generate a random number in the range [1, total_sum], inclusive
        randnum = random.randint(1, self.total_sum)
        
        # Use binary search to find the smallest index such that prefix_sums[index] >= randnum
        # This ensures that indices with higher weights have a higher chance of being selected
        idx = bisect.bisect_left(self.prefix_sums, randnum)
        
        # Return the selected index
        return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()