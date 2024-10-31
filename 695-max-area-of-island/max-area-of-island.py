class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Set to track visited cells to avoid reprocessing
        seen = set()
        
        # Get the number of rows and columns in the grid
        rows = len(grid)
        cols = len(grid[0])
        
        # Variable to store the maximum area found
        maxArea = 0
        
        # Possible 4-directional moves (right, down, left, up)
        neighbour = [(0,1), (1,0), (-1,0), (0,-1)]

        # Function to find all land cells (1s) in the current island and calculate its area
        def findneighbours(x, y):
            islandarea = 1  # Start with a base area of 1 for the initial cell
            queue = deque([(x, y)])  # Queue for BFS starting from cell (x, y)
            idxes = [(x, y)]  # Track cells that are part of the current island

            while queue:
                x0, y0 = queue.popleft()
                # Check each neighbor of the current cell
                for dx, dy in neighbour:
                    # Skip if the neighbor has been visited
                    if (x0 + dx, y0 + dy) in seen:
                        continue
                    # Check if the neighbor is within bounds and is land (1)
                    if 0 <= x0 + dx < rows and 0 <= y0 + dy < cols:
                        seen.add((x0 + dx, y0 + dy))
                        if grid[x0 + dx][y0 + dy] == 1:
                            islandarea += 1  # Increment area for each land cell found
                            queue.append((x0 + dx, y0 + dy))  # Add to queue for further exploration
                            idxes.append((x0 + dx, y0 + dy))  # Track all cells in the island

            return islandarea  # Return the total area of the island

        # Initialize a queue with all grid points
        idx = deque()
        for r in range(rows):
            for c in range(cols):
                idx.append((r, c))

        # Traverse each cell in the grid
        while idx:
            i, j = idx.popleft()
            # Skip if the cell has already been visited
            if (i, j) in seen:
                continue
            seen.add((i, j))
            # If the cell is land (1), calculate the area of the island starting from this cell
            if grid[i][j] == 1:
                area = findneighbours(i, j)
                # Update maxArea if the current island's area is larger
                if area > maxArea:
                    maxArea = area
        
        # Return the largest area found
        return maxArea

        