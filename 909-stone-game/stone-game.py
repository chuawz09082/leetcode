class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # If there is only one pile, the player wins by default since they can take the only pile.
        if len(piles) == 1:
            return True

        # Memoization dictionary to store intermediate results and avoid redundant calculations.
        memo = {}

        # Calculate the total sum of all stones in the piles.
        total = sum(piles)

        def helper(stones: List[int], number: int) -> bool:
            """
            Helper function to determine if the current player can win given the remaining stones.
            @param stones: The remaining piles of stones.
            @param number: The current player's accumulated score.
            @return: True if the current player can win, otherwise False.
            """
            # Check if the current state has already been computed and stored in the memo.
            if tuple(stones) in memo:
                return memo[tuple(stones)]

            # Base case: If there are only two piles left, the player picks the maximum of the two.
            if len(stones) == 2:
                maxstone = max(stones)
                # Check if the current player's total score after picking the maximum stone
                # is greater than the opponent's possible score.
                if number + maxstone > total - number - maxstone:
                    memo[tuple(stones)] = True
                else:
                    memo[tuple(stones)] = False
                return memo[tuple(stones)]
            
            # Recursive case: The current player picks either the first or last pile and calculates the result.
            # The player wins if either choice leads to a win.
            memo[tuple(stones)] = (
                helper(stones[1:], number + stones[0]) or  # Choose the first pile.
                helper(stones[:len(stones)-1], number + stones[-1])  # Choose the last pile.
            )
            return memo[tuple(stones)]

        # Start the helper function with the initial piles and a score of 0 for the first player.
        return helper(piles, 0)
            