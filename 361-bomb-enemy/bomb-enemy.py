class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        """
        Finds the maximum number of enemies that can be killed by placing a bomb at an empty cell ('0') 
        in the given grid. Enemies ('E') are blocked by walls ('W') in all four directions.

        Args:
        grid (List[List[str]]): 2D grid containing 'E' (enemies), 'W' (walls), and '0' (empty cells).

        Returns:
        int: Maximum number of enemies killed from one bomb placement.
        """
        # Initialize the maximum number of enemies killed
        maxkilled = 0
        # Dictionary to store the number of enemies that can be killed from each empty cell
        hashmap = collections.defaultdict(int)
        
        def helper(row: int, col: int):
            """
            Helper function to calculate the number of enemies that can be killed by 
            placing a bomb in an empty cell in all four directions.

            Args:
            row (int): Row index of the enemy ('E') cell.
            col (int): Column index of the enemy ('E') cell.
            """
            # Check upward direction
            for i in range(row - 1, -1, -1):  # Traverse upwards
                if grid[i][col] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(i, col)] += 1
                if grid[i][col] == "W":  # Stop at a wall
                    break

            # Check downward direction
            for i in range(row + 1, len(grid)):  # Traverse downwards
                if grid[i][col] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(i, col)] += 1
                if grid[i][col] == "W":  # Stop at a wall
                    break

            # Check left direction
            for j in range(col - 1, -1, -1):  # Traverse left
                if grid[row][j] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(row, j)] += 1
                if grid[row][j] == "W":  # Stop at a wall
                    break

            # Check right direction
            for j in range(col + 1, len(grid[0])):  # Traverse right
                if grid[row][j] == "0":  # If it's an empty cell, increment its count in the hashmap
                    hashmap[(row, j)] += 1
                if grid[row][j] == "W":  # Stop at a wall
                    break

        # Traverse the entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "E":  # If the current cell contains an enemy
                    helper(i, j)  # Calculate potential kills from all surrounding empty cells

        # If there are no valid empty cells, return 0
        if not hashmap.values():
            return 0

        # Return the maximum number of enemies that can be killed from a single empty cell
        return max(hashmap.values())
            


            


        