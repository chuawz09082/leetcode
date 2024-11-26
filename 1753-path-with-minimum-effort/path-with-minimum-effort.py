class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Define movement directions: down, up, right, left
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # Get the dimensions of the grid
        row = len(heights)
        col = len(heights[0])

        # Initialize a 2D array to store the minimum effort to reach each cell
        # Start with infinity for all cells, as we haven't visited them yet
        efforts = [[float('inf') for j in range(col)] for i in range(row)]
        
        # Use a min-heap to prioritize cells with the least effort
        # Start with the top-left cell (0,0) with effort 0
        heap = [(0, 0, 0)]  # Format: (effort, x, y)
        
        # Set the initial effort to reach the starting cell (0,0) as 0
        efforts[0][0] = 0

        # Process the heap until it's empty
        while heap:
            # Extract the cell with the minimum effort
            current_effort, x, y = heapq.heappop(heap)

            # Explore all valid neighboring cells
            for n in neighbours:
                xnew = x + n[0]  # Calculate the new x-coordinate
                ynew = y + n[1]  # Calculate the new y-coordinate
                
                # Check if the new cell is within bounds
                if 0 <= xnew < row and 0 <= ynew < col:
                    # Calculate the effort required to move to the new cell
                    effort_new = max(current_effort, abs(heights[xnew][ynew] - heights[x][y]))
                    
                    # If this effort is less than the previously recorded effort, update
                    if effort_new < efforts[xnew][ynew]:
                        efforts[xnew][ynew] = effort_new  # Update the effort for the new cell
                        # Push the new cell into the heap for further processing
                        heapq.heappush(heap, (effort_new, xnew, ynew))

        # Return the minimum effort required to reach the bottom-right cell
        return efforts[row - 1][col - 1]
            
