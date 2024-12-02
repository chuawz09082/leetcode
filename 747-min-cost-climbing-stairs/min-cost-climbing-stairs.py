class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Calculates the minimum cost to climb to the top of the stairs.

        Args:
        cost (List[int]): A list where cost[i] is the cost of step i.

        Returns:
        int: The minimum cost to reach the top of the staircase.
        """
        # Initialize a list to store the minimum cost to reach each step
        storecost = [0 for _ in range(len(cost))]

        # Base cases: The cost to reach the first and second steps
        storecost[0] = cost[0]
        storecost[1] = cost[1]

        # If there are more than 2 steps, compute the minimum cost for each step
        if len(cost) > 2:
            for i in range(2, len(cost)):
                # The cost to reach the current step is the cost of the step itself
                # plus the minimum cost of reaching either of the two previous steps
                storecost[i] = cost[i] + min(storecost[i - 1], storecost[i - 2])

        # The minimum cost to reach the top is the smaller of the costs to reach
        # the last two steps, as you can stop at either of them to finish the climb
        return min(storecost[-1], storecost[-2])
