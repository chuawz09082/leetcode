class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Edge case: If the matrix is empty, return an empty list
        if not matrix:
            return []

        rows = len(matrix)  # Total number of rows in the matrix
        cols = len(matrix[0])  # Total number of columns in the matrix
        seen = set()  # Set to keep track of visited positions (row, col)

        result = [matrix[0][0]]  # Initialize result with the first element of the matrix
        seen.add((0, 0))  # Mark the first element as visited

        # Define movement directions: right, down, left, up
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Initialize current position at the top-left corner
        row = 0
        col = 0

        # Continue the process until we've visited all elements in the matrix
        while len(result) < rows * cols:
            for dr, dc in steps:
                # Move in the current direction (right, down, left, or up)
                row += dr
                col += dc

                # Keep moving in the same direction while within bounds and the cell hasn't been visited
                while 0 <= row < rows and 0 <= col < cols and (row, col) not in seen:
                    result.append(matrix[row][col])  # Add the current element to the result
                    seen.add((row, col))  # Mark the current cell as visited
                    row += dr  # Move to the next row in the same direction
                    col += dc  # Move to the next column in the same direction

                # After hitting a boundary or a visited cell, step back to the last valid position
                row -= dr
                col -= dc

        return result

                



