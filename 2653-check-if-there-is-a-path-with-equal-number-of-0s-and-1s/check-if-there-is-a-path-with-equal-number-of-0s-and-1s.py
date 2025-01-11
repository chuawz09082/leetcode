class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        """
        Determines if there exists a path from the top-left to the bottom-right of the grid
        such that the number of 0s equals the number of 1s along the path.
        
        @param grid: 2D list of integers (0s and 1s).
        @return: True if a valid path exists, False otherwise.
        """
        rows, cols = len(grid), len(grid[0])

        # Dynamic programming table to track if the (r, c) cell is reachable with a balanced path
        dp = [[False] * cols for _ in range(rows)]

        # Set to track visited states to avoid redundant calculations
        visited = set()

        # If the total path length is odd, it is impossible to balance 0s and 1s
        if (rows + cols - 1) % 2 != 0:
            return False
        
        def dfs(r, c, count0, count1):
            """
            Depth-first search function to explore all paths from the top-left to the bottom-right.
            
            @param r: Current row index.
            @param c: Current column index.
            @param count0: Count of 0s encountered so far.
            @param count1: Count of 1s encountered so far.
            """
            # Base case: Out of bounds or already visited this state
            if r < 0 or r >= rows or c < 0 or c >= cols or dp[r][c] or (r, c, count0 - count1) in visited:
                return
            
            # Mark the current state as visited
            visited.add((r, c, count0 - count1))

            # Update the count of 0s or 1s based on the current cell value
            if grid[r][c] == 0:
                count0 += 1
            else:
                count1 += 1
            
            # If the counts of 0s and 1s are equal at this cell, mark it as reachable
            if count0 == count1:
                dp[r][c] = True
            
            # Recursive calls to explore the right and down neighbors
            dfs(r + 1, c, count0, count1)  # Move down
            dfs(r, c + 1, count0, count1)  # Move right

        # Start DFS from the top-left corner of the grid
        dfs(0, 0, 0, 0)

        # Return whether the bottom-right cell is reachable with a balanced path
        return dp[rows - 1][cols - 1]


            
            
        
        dfs(0,0,0,0)
        
