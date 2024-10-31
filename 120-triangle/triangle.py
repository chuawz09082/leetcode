class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Number of rows in the triangle
        row = len(triangle)
        
        # Initialize a memoization array with the last row of the triangle
        # This array will hold the minimum path sums from bottom to top
        memo = triangle[row - 1].copy()
        
        # Start from the second-last row and move upward to the top row
        for r in range(row - 2, -1, -1):
            # For each element in the current row, calculate the minimum path sum
            for c in range(r + 1):
                # Update memo[c] to be the minimum path sum from triangle[r][c]
                # by adding the current element and choosing the minimum of the paths below
                memo[c] = min(memo[c], memo[c + 1]) + triangle[r][c]
        
        # The top element in the memo array now holds the minimum path sum from top to bottom
        return memo[0]



        