class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        rows = len(grid)
        cols = len(grid[0])

        # Define possible 4-directional moves (down, up, right, left)
        neighbours = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Initialize a queue for BFS, a set to track visited cells, and a counter for oranges
        queue = deque()
        seen = set()
        num_of_oranges = 0

        # Initialize the minimum time to -1 to indicate no time has been taken yet
        mintime = -1

        # Traverse the grid to count oranges and identify initially rotten oranges
        for i in range(rows):
            for j in range(cols):
                # Count all oranges (1 for fresh, 2 for rotten)
                if grid[i][j] > 0:
                    num_of_oranges += 1
                    # Add rotten oranges to the queue with their position and starting time 0
                    if grid[i][j] == 2:
                        queue.append((i, j, 0))

        # If there are no oranges, return 0 as no rotting process is needed
        if num_of_oranges == 0:
            return 0

        # BFS to rot the oranges
        while queue:
            xpos, ypos, time = queue.popleft()

            # Skip if the cell has already been visited
            if (xpos, ypos) in seen:
                continue
            
            # Mark the cell as visited
            seen.add((xpos, ypos))

            # Check if all oranges have been reached, and update the minimum time
            if len(seen) == num_of_oranges and ((mintime > 0 and time < mintime) or mintime == -1):
                mintime = time

            # Explore each neighbor to spread the rot to adjacent fresh oranges
            for n in neighbours:
                new_x, new_y = xpos + n[0], ypos + n[1]
                # Ensure the neighbor is within grid bounds, is a fresh orange, and hasn’t been visited
                if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x][new_y] == 1 and (new_x, new_y) not in seen:
                    # Append the neighbor to the queue with incremented time
                    queue.append((new_x, new_y, time + 1))

        # Return the minimum time if all oranges were reached, otherwise return -1 (if some remain fresh)
        return mintime