class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb `n` stairs,
        where you can climb either 1 or 2 steps at a time.

        Args:
        n (int): The total number of stairs to climb.

        Returns:
        int: The number of distinct ways to climb the stairs.
        """
        # Initialize a hashmap to store precomputed results for base cases
        hashmap = {1: 1, 2: 2}  # 1 stair has 1 way, 2 stairs have 2 ways

        def helper(k: int) -> int:
            """
            Recursively computes the number of ways to climb `k` stairs,
            using memoization to store intermediate results.

            Args:
            k (int): The number of stairs to compute.

            Returns:
            int: The number of ways to climb `k` stairs.
            """
            # If the result for `k` stairs is already computed, return it
            if k in hashmap:
                return hashmap[k]

            # Compute the result for `k` stairs using the recurrence relation
            # Ways to climb `k` stairs = ways to climb `k-1` + ways to climb `k-2`
            hashmap[k] = helper(k - 1) + helper(k - 2)

            # Return the computed result for `k` stairs
            return hashmap[k]

        # Start the computation for `n` stairs
        return helper(n)
        
