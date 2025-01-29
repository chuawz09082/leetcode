class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
         # Get the size of the input grid
        n = len(grid)
        
        # Expand the grid: each original cell is represented by a 3x3 subgrid
        newgrid = [[0] * (3 * n) for _ in range(3 * n)]

        # Convert the original n x n grid into a 3n x 3n grid
        # '/' is represented as:
        #   0 0 1
        #   0 1 0
        #   1 0 0
        # '\' is represented as:
        #   1 0 0
        #   0 1 0
        #   0 0 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    newgrid[3 * i][3 * j + 2] = 1  # Top-right
                    newgrid[3 * i + 1][3 * j + 1] = 1  # Center
                    newgrid[3 * i + 2][3 * j] = 1  # Bottom-left
                elif grid[i][j] == '\\':
                    newgrid[3 * i][3 * j] = 1  # Top-left
                    newgrid[3 * i + 1][3 * j + 1] = 1  # Center
                    newgrid[3 * i + 2][3 * j + 2] = 1  # Bottom-right

        # Depth-first search function to explore empty regions
        def dfs(row, col):
            for nx, ny in neighbours:
                newrow = row + nx
                newcol = col + ny
                # Ensure the new cell is within bounds and has not been visited
                if 0 <= newrow < 3 * n and 0 <= newcol < 3 * n and (newrow, newcol) not in seen:
                    seen.add((newrow, newcol))  # Mark as visited
                    if newgrid[newrow][newcol] == 0:  # Continue DFS only if the cell is empty
                        dfs(newrow, newcol)

        # Set to keep track of visited cells
        seen = set()
        # Define movement directions (right, left, down, up)
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # Count the number of connected components (regions)
        count = 0

        # Iterate through the expanded 3n x 3n grid
        for x in range(3 * n):
            for y in range(3 * n):
                if (x, y) in seen:  # Skip already visited cells
                    continue
                if newgrid[x][y] == 0 and (x, y) not in seen:  # Start a new region if it's empty
                    seen.add((x, y))  # Mark the starting cell as visited
                    count += 1  # Increase the region count
                    dfs(x, y)  # Explore the region using DFS
                seen.add((x, y))  # Mark the current cell as visited

        return count  # Return the total number of regions       