class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        # Define possible directions for moving: up, left, right, down
        neighbours = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        # Initialize a max-heap (using negative values for Python's min-heap implementation)
        heap = [(-grid[0][0], 0, 0)]  # Start with the top-left corner value, negated
        seen = set()  # Set to track visited cells
        seen.add((0, 0))  # Mark the starting cell as visited
        
        # Initialize the minimum score with the value at the starting cell
        minscore = grid[0][0]
        
        while heap:
            # Extract the cell with the maximum value (smallest negative value)
            current, x, y = heapq.heappop(heap)
            current = -current  # Negate to get the actual value
            
            # Update the minimum score encountered so far
            minscore = min(current, minscore)
            
            # If the bottom-right corner is reached, return the minimum score
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return minscore
            
            # Explore all valid neighbors
            for n in neighbours:
                xnew = x + n[0]  # Compute new x-coordinate
                ynew = y + n[1]  # Compute new y-coordinate
                
                # Check if the new cell is within bounds and not visited
                if 0 <= xnew < len(grid) and 0 <= ynew < len(grid[0]) and (xnew, ynew) not in seen:
                    seen.add((xnew, ynew))  # Mark the cell as visited
                    # Push the new cell's value (negated) and its coordinates into the heap
                    heapq.heappush(heap, (-grid[xnew][ynew], xnew, ynew))
        
        return minscore  # Return the minimum score (though the loop should always exit earlier)
