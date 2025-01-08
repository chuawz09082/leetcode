class Solution:
    def maxScore(self, n: int, k: int, stayScore: List[List[int]], travelScore: List[List[int]]) -> int:
        """
        Finds the maximum score achievable in `k` days while staying or traveling between `n` cities.

        @param n: int - The number of cities.
        @param k: int - The number of days.
        @param stayScore: List[List[int]] - A 2D list where stayScore[i][j] represents the score obtained by staying
                                            in city `j` on day `i`.
        @param travelScore: List[List[int]] - A 2D list where travelScore[i][j] represents the score obtained by
                                              traveling from city `i` to city `j`.
        @return: int - The maximum score achievable after `k` days.
        """
        # Step 1: Initialize a DP table where dp[i][j] represents the maximum score achievable on day `i`
        #         if you are in city `j`.
        dp = [[0] * n for _ in range(k + 1)]  # Rows represent days, columns represent cities.

        # Step 2: Iterate through the days from day 1 to day `k`.
        for i in range(1, k + 1):
            # Step 3: For each city `j`, calculate the maximum score on day `i` if you stay in or travel to `j`.
            for j in range(n):
                # Case 1: Stay in the same city `j`.
                dp[i][j] = dp[i - 1][j] + stayScore[i - 1][j]

                # Case 2: Travel to city `j` from any other city `k`.
                #         Compute the score for traveling from each city `k` (where `k != j`) to city `j`.
                alltravel = [dp[i - 1][k] + travelScore[k][j] for k in range(n) if k != j]
                if alltravel:
                    # Update the maximum score for city `j` on day `i` if traveling yields a higher score.
                    dp[i][j] = max(dp[i][j], max(alltravel))

        # Step 4: Return the maximum score achievable on the last day across all cities.
        return max(dp[-1])
        