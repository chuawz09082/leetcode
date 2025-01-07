class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        """
        Finds the longest square streak in a list of integers. A square streak means a sequence where
        each number is the square of the previous one.

        @param nums: List[int] - List of integers.
        @return: int - Length of the longest square streak, or -1 if no streak longer than 1 exists.
        """
        # Step 1: Sort the input list to process numbers in ascending order.
        sorted_nums = sorted(nums)

        # Step 2: Initialize a dictionary to store the length of the square streak for each number.
        # Default value is 0.
        dp = collections.defaultdict(int)

        # Step 3: Iterate through the sorted list of numbers.
        for num in sorted_nums:
            # Calculate the integer square root of the current number.
            sqrt_num = int(math.sqrt(num))
            
            # Step 4: Check if the number is a perfect square.
            # If the square of `sqrt_num` equals `num`, it is part of a square streak.
            if sqrt_num * sqrt_num == num:
                # Update the streak length for the current number based on its square root.
                dp[num] = dp[sqrt_num] + 1
            else:
                # If not a perfect square, it starts its own streak of length 1.
                dp[num] = 1

        # Step 5: If the maximum streak length is 1, no valid square streak exists.
        if max(list(dp.values())) == 1:
            return -1
        
        # Step 6: Return the maximum streak length from the dictionary.
        return max(list(dp.values()))

            
        