class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """
        Finds the k-th integer in the range [lo, hi] when sorted by their power value.
        If two integers have the same power value, they are sorted by their value.

        Power value is calculated using the following rules:
        - If x is even, x = x / 2
        - If x is odd, x = 3 * x + 1
        - Repeat the process until x becomes 1, and count the number of steps.

        Args:
        lo (int): Lower bound of the range.
        hi (int): Upper bound of the range.
        k (int): Position (1-based) in the sorted list to return.

        Returns:
        int: The k-th integer in the sorted list.
        """
        # Cache to store computed power values for integers
        dp = {1: 0}  # Base case: Power of 1 is 0
        power = {}  # Dictionary to store power values for integers in [lo, hi]

        def helper(x):
            """
            Recursively computes the power value for integer x using memoization.

            Args:
            x (int): The integer whose power value is to be computed.

            Returns:
            int: The power value of x.
            """
            if x in dp:
                # Return cached power value if it has already been computed
                return dp[x]
            if x % 2 == 0:
                # If x is even, compute power for x / 2
                dp[x] = 1 + helper(x // 2)
            else:
                # If x is odd, compute power for 3 * x + 1
                dp[x] = 1 + helper(3 * x + 1)
            return dp[x]

        # Calculate power values for all integers in the range [lo, hi]
        for i in range(lo, hi + 1):
            power[i] = helper(i)

        # Sort integers by their power value, and if equal, by their value
        sortlist = sorted(list(power.items()), key=lambda x: (x[1], x[0]))
        
        # Extract the sorted integers
        keys = [key[0] for key in sortlist]

        # Return the k-th integer (1-based index)
        return keys[k - 1]
        