class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # Dictionary to count the frequency of brick edge positions.
        # The key is the position from the left, and the value is the count of how many rows have an edge at that position.
        memo = collections.defaultdict(int)

        # Iterate through each row in the wall
        for row in wall:
            startsum = 0  # This keeps track of the position from the left edge of the wall
            
            # We exclude the last brick in each row because the edge of the wall doesn't count
            for i in range(len(row) - 1):
                startsum += row[i]  # Add the brick's width to the cumulative sum to get the edge position
                memo[startsum] += 1  # Increment the count of edges at this position
        
        # If memo is empty, it means no edge positions were recorded, 
        # implying every row is a single brick, so the line will cross all rows.
        if not memo:
            return len(wall)
        
        # Find the maximum value in memo, which represents the position 
        # where the most edges align (i.e., the optimal position to draw a line)
        maxvalue = max(memo.values())
        
        # The least number of bricks crossed is the total number of rows 
        # minus the number of edges at the optimal position.
        return len(wall) - maxvalue


        