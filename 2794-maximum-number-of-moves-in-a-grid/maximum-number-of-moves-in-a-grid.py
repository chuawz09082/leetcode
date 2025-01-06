class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum number of moves you can perform in the grid by starting
        from any cell in the first column and moving to cells in subsequent columns
        such that the cell you move to has a strictly higher value.
        
        @param grid: List[List[int]] - 2D grid of positive integers.
        @return: int - Maximum number of moves possible.
        """

        # Initialize a DP table with the same dimensions as the grid.
        # dp[row][col] will store the maximum number of moves to reach grid[row][col].
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        maxmoves = 0  # Variable to track the global maximum number of moves.

        # Iterate over columns starting from the second column.
        for col in range(1, len(grid[0])):
            # Iterate over each row in the current column.
            for row in range(len(grid)):

                # Check neighbors in the previous column for valid moves.
                for dr in [-1, 0, 1]:  # Neighbor row offsets: -1 (above), 0 (same row), +1 (below)
                    neighbor_row = row + dr
                    neighbor_col = col - 1

                    # Check if the neighbor is within the grid bounds.
                    if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
                        # Ensure the neighbor has a smaller value and the move is valid.
                        if grid[neighbor_row][neighbor_col] < grid[row][col] and dp[neighbor_row][neighbor_col] == col - 1:
                            # Update the current cell in the DP table with the maximum moves.
                            dp[row][col] = max(dp[row][col], dp[neighbor_row][neighbor_col] + 1)

                # Update the global maximum number of moves.
                maxmoves = max(maxmoves, dp[row][col])

        # Return the maximum moves found.
        return maxmoves

        