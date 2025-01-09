class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        """
        Constructs a matrix such that the row sums match `rowSum` and the column sums match `colSum`.

        @param rowSum: List[int] - List representing the sum of each row.
        @param colSum: List[int] - List representing the sum of each column.
        @return: List[List[int]] - A matrix that satisfies the row and column sum constraints.
        """
        # Initialize the matrix with zeros
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for _ in range(rows)]

        # Use a greedy approach to construct the matrix
        for i in range(rows):
            for j in range(cols):
                # Fill the current cell with the minimum of the remaining row and column sums
                matrix[i][j] = min(rowSum[i], colSum[j])
                
                # Update the remaining sums
                rowSum[i] -= matrix[i][j]
                colSum[j] -= matrix[i][j]

        return matrix