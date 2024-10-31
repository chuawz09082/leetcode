class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # Set to store unique island shapes as frozensets
        seenislands = set()
        
        # Set to track the coordinates that have been visited
        seenpoints = set()
        
        # Queue to store all grid points (for breadth-first traversal)
        idxes = deque()

        rows = len(grid)   # Number of rows in the grid
        cols = len(grid[0]) # Number of columns in the grid

        # Possible 4-directional moves (right, down, left, up)
        neighbour = [(0,1),(1,0),(-1,0),(0,-1)]

        # Helper function to find the minimum tuple in a list of tuples
        def findmin(elements):   
            min_element = min(elements, key=lambda x: (x[0], x[1]))   
            return min_element
        
        # Function to find all neighboring land (1s) of a given cell
        def findneighbours(x, y):
            island = set()
            island.add((x, y))
            queue = deque([(x, y)])

            while queue:
                x0, y0 = queue.popleft()
                # Check all neighbors of the current cell
                for dx, dy in neighbour:
                    if (x0 + dx, y0 + dy) in seenpoints:
                        continue
                    if 0 <= x0 + dx < rows and 0 <= y0 + dy < cols:
                        seenpoints.add((x0 + dx, y0 + dy))
                        # If the neighbor is land, add it to the island set and queue
                        if grid[x0 + dx][y0 + dy] == 1:
                            island.add((x0 + dx, y0 + dy))
                            queue.append((x0 + dx, y0 + dy))

            return list(island)

        # Helper function to shift all points in `lst` by `subtrahend` to normalize
        def subtract_tuple_from_list(lst, subtrahend):
            return [(x - subtrahend[0], y - subtrahend[1]) for x, y in lst]

        # Initialize the queue with all grid points
        for r in range(rows):
            for c in range(cols):
                idxes.append((r, c))

        # Traverse each cell in the grid
        while idxes:
            i, j = idxes.popleft()
            # Skip if the cell has been seen
            if (i, j) in seenpoints:
                continue
            seenpoints.add((i, j))
            # If the cell is land (1), find its neighbors and define the island
            if grid[i][j] == 1:
                listisland = findneighbours(i, j)
                # Normalize the island by finding the minimum point and adjusting all points relative to it
                mintuple = findmin(listisland)
                listisland = subtract_tuple_from_list(listisland, mintuple)
                # Store the unique island shape as a frozenset
                seenislands.add(frozenset(listisland))

        # Return the count of unique island shapes
        return len(seenislands)







