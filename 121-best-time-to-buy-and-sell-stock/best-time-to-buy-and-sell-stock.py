class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved from a single stock trade.
        You can only buy once and sell once.

        Args:
        prices (List[int]): A list where prices[i] is the price of a given stock on day i.

        Returns:
        int: The maximum profit you can achieve. If no profit is possible, returns 0.
        """
        # Initialize the minimum cost (lowest price encountered so far) to the first day's price
        cost = prices[0]
        # Initialize the maximum profit to 0
        profit = 0

        # Iterate through the prices starting from the second day
        for curr in prices[1:]:
            # If the current price is lower than the recorded cost, update the cost
            if curr < cost:
                cost = curr
            else:
                # Calculate the profit for the current price and update max profit if it's higher
                profit = max(profit, curr - cost)

        # Return the maximum profit calculated
        return profit

        
            



        