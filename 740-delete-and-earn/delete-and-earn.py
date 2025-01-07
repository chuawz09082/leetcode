class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        """
        Solves the problem using a dynamic programming approach similar to the "House Robber" problem.

        @param nums: List[int] - A list of integers representing the values of numbers to process.
        @return: int - The maximum points that can be earned.
        """
        # Step 1: Count the occurrences of each number in the input list.
        count = Counter(nums)
        
        # Step 2: Create a sorted list of unique numbers in nums.
        # This ensures we process numbers in increasing order.
        heap = sorted(list(count.keys()))

        # Step 3: Initialize a DP array to store the maximum points at each value.
        # The size of the DP array is the maximum number in the heap + 1.
        dp = [0 for _ in range(max(heap) + 1)]

        # Step 4: Iterate through all possible numbers from 1 to max(heap).
        for curr in range(1, max(heap) + 1):
            if curr == 1:
                # Base case: For value 1, the maximum points are simply its frequency times its value.
                dp[curr] = count[curr]
            else:
                # Transition relation:
                # - Option 1: Skip the current number and take the value of dp[curr-1].
                # - Option 2: Take the current number (curr) and add its value to dp[curr-2].
                #   dp[curr-2] ensures that we avoid adding adjacent numbers.
                dp[curr] = max(dp[curr - 1], dp[curr - 2] + curr * count[curr])

        # Step 5: Return the maximum points, which is stored in dp[-1].
        return dp[-1]
        





        