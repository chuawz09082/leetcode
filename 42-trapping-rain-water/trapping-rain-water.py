class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the total amount of trapped rainwater using increasing and decreasing height lists.
        
        @param height: List[int] - Heights of the bars in the histogram.
        @return: int - Total amount of trapped rainwater.
        """
        length = len(height)
        increasing = []  # To store indices of increasing height bars.
        decreasing = []  # To store indices of decreasing height bars.
        dp = [0] * length  # To store the trapped water at each index.

        # Step 1: Identify indices for increasing and decreasing heights.
        for i in range(length):
            if height[i] == 0:
                continue  # Skip indices with height 0 (no trapping possible here).
            
            # Maintain the increasing stack:
            # Append indices where heights are greater than or equal to the previous index's height.
            if not increasing or height[i] >= height[increasing[-1]]:
                increasing.append(i)

            # Maintain the decreasing stack:
            # Pop indices where the current height is greater than the height at the top of the stack.
            while decreasing and height[decreasing[-1]] < height[i]:
                decreasing.pop()

            # Append the current index to the decreasing stack.
            decreasing.append(i)

        # Step 2: Calculate trapped water for the increasing height pairs.
        for i, j in zip(increasing[:length - 1], increasing[1:]):
            # Calculate the maximum water level between two indices.
            water = min(height[i], height[j])
            # Calculate trapped water for each index between `i` and `j`.
            for k in range(i + 1, j):
                dp[k] = max(dp[k], water - height[k])

        # Step 3: Calculate trapped water for the decreasing height pairs.
        for i, j in zip(decreasing[:length - 1], decreasing[1:]):
            # Calculate the maximum water level between two indices.
            water = min(height[i], height[j])
            # Calculate trapped water for each index between `i` and `j`.
            for k in range(i + 1, j):
                dp[k] = max(dp[k], water - height[k])

        # Step 4: Return the total trapped water.
        return sum(dp)


        