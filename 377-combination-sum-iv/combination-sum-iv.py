class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Sort the numbers to facilitate early stopping in loops
        nums.sort()
        
        # If the smallest number in nums is greater than the target,
        # it's impossible to form the target, so return 0
        if min(nums) > target:
            return 0
        
        # Initialize a DP table (hash) where hash[i] represents the number of ways
        # to form the sum i using elements from nums
        hash = [0 for _ in range(target + 1)]

        # Populate the DP table for sums that can be directly formed by numbers in nums
        for num in nums:
            if num <= target:
                hash[num] += 1  # There is one way to form 'num' using itself

        # Iterate over all possible sums from the smallest number to target
        for pos in range(nums[0], target):
            # Skip if the current sum 'pos' cannot be formed
            if hash[pos] == 0:
                continue
            
            # For each number in nums, calculate the new sum (pos + num)
            # and update the DP table if the new sum is within bounds
            for num in nums:
                if pos + num <= target:
                    hash[pos + num] += hash[pos]  # Add the number of ways to form 'pos' to 'pos + num'
                else:
                    break  # Stop early as nums is sorted and further sums will exceed target

        # The result is the number of ways to form the target sum
        return hash[target]
