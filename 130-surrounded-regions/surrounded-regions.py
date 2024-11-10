class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modifies the given board in-place by capturing surrounded regions.
        """
        
        # Directions for exploring neighbors (right, left, down, up)
        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Set to track visited cells
        seen = set()
        
        # Dimensions of the board
        rows = len(board)
        cols = len(board[0])

        # Depth-first search to explore regions of 'O' cells
        def dfs(row: int, col: int) -> None:
            # Stack to store cells in the current region and to mark as part of an island
            stack = [(row, col)]
            # Check list to explore neighboring cells
            check = [(row, col)]
            # Flag to determine if the current region is fully surrounded by 'X'
            island = True

            while check:
                # Pop the last cell to explore its neighbors
                row, col = check.pop()

                # Explore each neighboring cell
                for n in neighbours:
                    new_row, new_col = row + n[0], col + n[1]
                    
                    # Check if the neighbor is within board boundaries
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        # If neighbor is 'O' and not seen, mark it as part of the current region
                        if board[new_row][new_col] == "O" and (new_row, new_col) not in seen:
                            seen.add((new_row, new_col))
                            stack.append((new_row, new_col))
                            # If inside the boundaries, add it to `check` to explore further
                            if 0 < new_row < rows - 1 and 0 < new_col < cols - 1:
                                check.append((new_row, new_col))
                            else:
                                # If on a boundary, mark region as not an island
                                island = False
                        # If seen and located on boundary, it's not an island
                        if (new_row, new_col) in seen and ((new_row == 0 or new_row == rows - 1) or (new_col == 0 or new_col == cols - 1)):
                            island = False
            
            # If the entire region is an island, convert all cells to 'X'
            if island:
                for row, col in stack:
                    board[row][col] = "X"
        
        # Iterate through each cell on the board
        for i in range(rows):
            for j in range(cols):
                # Start a DFS if the cell is 'O' and hasn't been visited
                if board[i][j] == "O" and (i, j) not in seen:
                    seen.add((i, j))
                    # Only run DFS if 'O' is not on the boundary
                    if 0 < i < rows - 1 and 0 < j < cols - 1:
                        dfs(i, j)

        
