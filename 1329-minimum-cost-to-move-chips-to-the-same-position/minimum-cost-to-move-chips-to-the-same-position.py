class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        # Initialize counters for chips on odd and even positions
        odds = 0
        evens = 0

        # Iterate through each chip's position
        for pos in position:
            # If the position is even, increment the even counter
            if pos % 2 == 0:
                evens += 1
            # If the position is odd, increment the odd counter
            else:
                odds += 1
        
        # The minimum cost to move all chips to a single position is the smaller
        # of the number of chips on odd positions or even positions
        return min(odds, evens)
        