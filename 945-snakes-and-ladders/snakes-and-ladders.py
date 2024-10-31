class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # Helper function to add items to the queue with priority
        # This sorts items by prioritizing those closer to the end (higher pos) and then by moves
        def add_with_priority(queue, item):
            queue.append(item)
            queue = deque(sorted(queue, key=lambda x: (-x[0], x[1])))  # Sort by position descending, then by moves
            return queue

        # Dimensions of the board
        rows, cols = len(board), len(board[0])
        
        # Final position to reach on the board
        last = rows * cols - 1
        
        # Variable to store the minimum number of moves to reach the end
        minmoves = float('inf')
        
        # Flattened board representation to simplify index handling
        new_board = []
        for i in range(rows - 1, -1, -1):
            row = board[i]
            # Alternate row reversal for correct "snakes and ladders" board traversal
            if (rows - 1 - i) % 2 == 1:
                row.reverse()
            new_board += row
        
        # Queue for BFS, initialized with the starting position (0,0), meaning 0th square with 0 moves
        queue = deque([(0, 0)])
        
        # Dictionary to track the minimum moves to reach each position
        seen = {0: 0}

        # BFS loop to explore the board
        while queue:
            pos, moves = queue.popleft()  # Current position and number of moves taken to reach it

            # Check if we reached the last cell and update minmoves if this path is shorter
            if pos == last and moves < minmoves:
                minmoves = moves

            # Skip processing if this path has already exceeded the minimum moves found
            if moves >= minmoves:
                continue

            # Explore next positions within dice roll range (1 to 6 steps ahead)
            for newpos in range(pos + 1, min(pos + 6, last) + 1):
                # Check if there's a ladder or snake at newpos
                if new_board[newpos] - 1 >= 0 and (new_board[newpos] - 1 < pos + 1 or new_board[newpos] - 1 > min(pos + 6, last)):
                    # If ladder/snake leads to a position not seen before or with fewer moves, add it
                    if new_board[newpos] - 1 not in seen or seen[new_board[newpos] - 1] > moves + 1:
                        queue = add_with_priority(queue, (new_board[newpos] - 1, moves + 1))
                        seen[new_board[newpos] - 1] = moves + 1
                else:
                    # If moving directly to newpos without a ladder/snake, check if it’s better than seen paths
                    if newpos not in seen or seen[newpos] > moves + 1:
                        queue = add_with_priority(queue, (newpos, moves + 1))
                        seen[newpos] = moves + 1

        # If we found a path to the end within finite moves, return it; otherwise, return -1
        return minmoves if minmoves < float('inf') else -1


