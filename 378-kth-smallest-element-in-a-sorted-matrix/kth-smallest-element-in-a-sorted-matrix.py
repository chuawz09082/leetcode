class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
         # Min-heap to store elements in the form (value, row_index, col_index)
        queue = [(matrix[0][0], 0, 0)]
        heapq.heapify(queue)  # Convert the list into a valid heap

        # Possible directions to move: right (0,1) and down (1,0)
        neighbours = [(0, 1), (1, 0)]

        count = 0  # Counter to track the number of elements popped
        rows, cols = len(matrix), len(matrix[0])
        seen = set()  # Set to keep track of visited positions in the matrix

        while count < k and queue:
            # Extract the smallest element from the heap
            current, row, col = heappop(queue)
            count += 1

            # If we have popped k elements, return the k-th smallest element
            if count == k:
                return current

            # Explore the right and down neighbors
            for dx, dy in neighbours:
                newx, newy = row + dx, col + dy

                # Ensure the new position is within bounds and has not been visited
                if 0 <= newx < rows and 0 <= newy < cols and (newx, newy) not in seen:
                    # Push the new element into the heap
                    heappush(queue, (matrix[newx][newy], newx, newy))
                    seen.add((newx, newy))  # Mark it as visited
        


        


        